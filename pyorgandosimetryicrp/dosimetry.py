"""
Core dosimetry calculation module with wall/contents organ handling.
"""
import numpy as np
import pandas as pd
from typing import Dict, Optional
from scipy.integrate import trapz
from .config import (SOURCE_ORGANS, TARGET_ORGANS, WALL_CONTENT_PAIRS,
                    SECONDS_PER_HOUR, MBq_TO_Bq)
from .data_loader import DataLoader, SValueLoader

class DosimetryCalculator:
    """Class for performing dosimetry calculations."""
    
    def __init__(self, svalue_loader: Optional[SValueLoader] = None):
        self.svalue_loader = svalue_loader or SValueLoader()
    
    def calculate_from_timepoints(
        self,
        time_activity_data: pd.DataFrame,
        radionuclide: str
    ) -> Dict[str, float]:
        """
        Calculate organ doses from time-activity data.
        
        Args:
            time_activity_data: DataFrame with time points and organ activities
            radionuclide: Name of the radionuclide
            
        Returns:
            Dictionary of organ doses (Gy)
        """
        # Calculate number of disintegrations for each source organ
        disintegrations = {}
        for organ in SOURCE_ORGANS:
            times = time_activity_data['Time_Hours'].values * SECONDS_PER_HOUR
            activities = time_activity_data[organ].values * MBq_TO_Bq
            disintegrations[organ] = trapz(activities, times)
        
        return self.calculate_from_disintegrations(disintegrations, radionuclide)
    
    def calculate_from_disintegrations(
        self,
        disintegrations: Dict[str, float],
        radionuclide: str
    ) -> Dict[str, float]:
        """
        Calculate organ doses from number of disintegrations.
        
        Args:
            disintegrations: Dictionary of organ disintegrations
            radionuclide: Name of the radionuclide
            
        Returns:
            Dictionary of organ doses (Gy)
        """
        # Load S-values
        s_values = self.svalue_loader.load_svalue(radionuclide)
        
        # Calculate doses
        doses = {}
        for target_organ in TARGET_ORGANS:
            dose = 0.0
            
            # For wall organs, add contribution from contents
            if target_organ in WALL_CONTENT_PAIRS:
                contents = WALL_CONTENT_PAIRS[target_organ]
                if contents in disintegrations:
                    s_value = s_values.loc[target_organ, contents]
                    dose += disintegrations[contents] * s_value
            
            # Add contributions from all source organs
            for source_organ in SOURCE_ORGANS:
                if source_organ in disintegrations:
                    s_value = s_values.loc[target_organ, source_organ]
                    dose += disintegrations[source_organ] * s_value * 1e-3  # Convert mGy to Gy
                    
            doses[target_organ] = dose
            
        return doses