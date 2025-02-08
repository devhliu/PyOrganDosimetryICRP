from pyorgandosimetryicrp import DosimetryCalculator
from pyorgandosimetryicrp.data_loader import DataLoader

# Load time-activity data
data = DataLoader.load_time_activity_data('input_data.csv')

# Create calculator instance
calculator = DosimetryCalculator()

# Calculate doses from time-activity data