"""
Module for loading input data and S-values with wall/contents organ handling.
"""
import os
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Optional
from .config import (SOURCE_ORGANS, TARGET_ORGANS, RADIONUCLIDES, 
                    REQUIRED_COLUMNS, WALL_CONTENT_PAIRS)

class DataLoader:
    """Class for loading and validating input time-activity data."""
    
    @staticmethod
    def load_time_activity_data(filepath: str) -> pd.DataFrame:
        """
        Load time-activity data from CSV file.
        
        Args:
            filepath: Path to CSV file containing time-activity data
            
        Returns:
            DataFrame with time points as rows and source organs as columns
        """
        try:
            df = pd.read_csv(filepath)
            
            # Validate columns
            missing_cols = set(REQUIRED_COLUMNS) - set(df.columns)
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
            
            # Validate time values
            if not pd.to_numeric(df['Time_Hours'], errors='coerce').notna().all():
                raise ValueError("Time_Hours column contains non-numeric values")
            
            if not (df['Time_Hours'] >= 0).all():
                raise ValueError("Time_Hours contains negative values")
                
            # Validate activity values
            for organ in SOURCE_ORGANS:
                if not pd.to_numeric(df[organ], errors='coerce').notna().all():
                    raise ValueError(f"Non-numeric values found in {organ} column")
                if not (df[organ] >= 0).all():
                    raise ValueError(f"Negative values found in {organ} column")
            
            return df
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {filepath}")
        except Exception as e:
            raise ValueError(f"Error loading input data: {str(e)}")

class SValueLoader:
    """Class for loading and managing S-values."""
    
    def __init__(self):
        self.package_dir = Path(__file__).parent
        self.svalue_dir = self.package_dir / 'svalues'
        self.s_values: Dict[str, pd.DataFrame] = {}
    
    def load_svalue(self, radionuclide: str) -> pd.DataFrame:
        """
        Load S-values for a specific radionuclide.
        
        Args:
            radionuclide: Name of the radionuclide (e.g., 'F18')
            
        Returns:
            DataFrame containing S-values (mGy/MBq-s)
        """
        if radionuclide not in RADIONUCLIDES:
            raise ValueError(f"Unsupported radionuclide: {radionuclide}")
            
        if radionuclide in self.s_values:
            return self.s_values[radionuclide]
        
        file_path = self.svalue_dir / f"{radionuclide}.csv"
        if not file_path.exists():
            raise FileNotFoundError(f"S-value file not found: {file_path}")
            
        df = pd.read_csv(file_path, index_col=0)
        self._validate_svalue_data(df, radionuclide)
        self.s_values[radionuclide] = df
        return df
    
    def _validate_svalue_data(self, df: pd.DataFrame, radionuclide: str):
        """Validate S-value data format and content."""
        # Check required organs
        missing_sources = set(SOURCE_ORGANS) - set(df.columns)
        missing_targets = set(TARGET_ORGANS) - set(df.index)
        
        if missing_sources or missing_targets:
            raise ValueError(
                f"Missing organs in {radionuclide} S-value data:\n"
                f"Missing source organs: {missing_sources}\n"
                f"Missing target organs: {missing_targets}"
            )
        
        # Check wall-contents pairs
        for wall, contents in WALL_CONTENT_PAIRS.items():
            if wall not in df.index or contents not in df.columns:
                raise ValueError(
                    f"Missing wall-contents pair in {radionuclide} data:\n"
                    f"Wall: {wall}, Contents: {contents}"
                )
        
        # Check for negative or non-finite values
        if (df.values < 0).any():
            raise ValueError(f"Negative S-values found in {radionuclide} data")
        if not np.isfinite(df.values).all():
            raise ValueError(f"Non-finite S-values found in {radionuclide} data")