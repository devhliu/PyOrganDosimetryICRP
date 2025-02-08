"""
Configuration settings for the pyorgandosimetryicrp package.
"""

# Define wall/contents organ pairs
WALL_CONTENT_PAIRS = {
    'Gallbladder Wall': 'Gallbladder Contents',
    'LLI Wall': 'LLI Contents',
    'Small Intestine Wall': 'Small Intestine Contents',
    'Stomach Wall': 'Stomach Contents',
    'ULI Wall': 'ULI Contents',
    'Heart Wall': 'Heart Contents',
    'Urinary Bladder Wall': 'Urinary Bladder Contents'
}

# Standard source organs (including contents)
SOURCE_ORGANS = [
    'Adrenals',
    'Brain',
    'Breasts',
    'Gallbladder Contents',
    'LLI Contents',
    'Small Intestine Contents',
    'Stomach Contents',
    'ULI Contents',
    'Heart Contents',
    'Kidneys',
    'Liver',
    'Lungs',
    'Muscle',
    'Ovaries',
    'Pancreas',
    'Red Marrow',
    'Osteogenic Cells',
    'Skin',
    'Spleen',
    'Testes',
    'Thymus',
    'Thyroid',
    'Urinary Bladder Contents',
    'Uterus',
    'Total Body'
]

# Standard target organs (including walls)
TARGET_ORGANS = [
    'Adrenals',
    'Brain',
    'Breasts',
    'Gallbladder Wall',
    'LLI Wall',
    'Small Intestine Wall',
    'Stomach Wall',
    'ULI Wall',
    'Heart Wall',
    'Kidneys',
    'Liver',
    'Lungs',
    'Muscle',
    'Ovaries',
    'Pancreas',
    'Red Marrow',
    'Osteogenic Cells',
    'Skin',
    'Spleen',
    'Testes',
    'Thymus',
    'Thyroid',
    'Urinary Bladder Wall',
    'Uterus',
    'Total Body'
]

# List of supported radionuclides with their half-lives in hours
RADIONUCLIDES = {
    'F18': 1.83,      # 109.8 minutes
    'Ga68': 1.13,     # 67.8 minutes
    'Cu64': 12.7,     # 12.7 hours
    'Zr89': 78.41,    # 78.41 hours
    'I131': 192.48,   # 8.02 days
    'Lu177': 159.6,   # 6.65 days
    'Ac225': 240.0,   # 10.0 days
    'Pb212': 10.64    # 10.64 hours
}

# Required columns in input CSV
REQUIRED_COLUMNS = ['Time_Hours'] + SOURCE_ORGANS

# Physical constants
SECONDS_PER_HOUR = 3600
MBq_TO_Bq = 1e6