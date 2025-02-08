"""
Data models for organ data and time-activity curves.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional
import numpy as np

@dataclass
class TimeActivityData:
    """Class for storing time-activity data for an organ."""
    times: np.ndarray  # Time points in hours
    activities: np.ndarray  # Activity values in %ID
    organ_name: str
    
    def __post_init__(self):
        if len(self.times) != len(self.activities):
            raise ValueError("Times and activities must have the same length")
        if not all(self.times[i] <= self.times[i+1] for i in range(len(self.times)-1)):
            raise ValueError("Time points must be in ascending order")

@dataclass
class OrganData:
    """Class for storing organ-specific data."""
    name: str
    mass: float  # Mass in grams
    cumulated_activity: Optional[float] = None  # Number of disintegrations
    time_activity_data: Optional[TimeActivityData] = None
    
    def validate(self):
        """Validate organ data."""
        if self.cumulated_activity is None and self.time_activity_data is None:
            raise ValueError("Either cumulated activity or time-activity data must be provided")