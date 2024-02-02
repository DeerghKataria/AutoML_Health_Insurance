# 1. Import Necessary Libraries:

import pandas as pd
from tpot import TPOTRegressor

# 2. Load and Preprocess Data:

# Load the dataset
data = pd.read_csv("life_insurance_data.csv")

# Handle missing values, outliers, and feature engineering (if needed)
...

# Split data into training, validation, and test sets
train, valid, test = data.split_frames([0.7, 0.15])