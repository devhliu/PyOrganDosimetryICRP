"""
pyorgandosimetryicrp - Internal radiation dosimetry calculation package
Based on OLINDA 2.0 and ICRP 89 organ models
"""

from .dosimetry import DosimetryCalculator
from .data_loader import DataLoader, SValueLoader
from .models import OrganData, TimeActivityData

__version__ = "0.1.0"
__author__ = "devhliu"
__all__ = ['DosimetryCalculator', 'DataLoader', 'SValueLoader', 
           'OrganData', 'TimeActivityData']