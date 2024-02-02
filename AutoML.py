# 1. Import Necessary Libraries:
import pandas as pd
import h2o
from h2o.automl import H2OAutoML

# 2. Load and Preprocess Data:

# Load the dataset
data = pd.read_csv("life_insurance_data.csv")

# Initialize and start H2O
h2o.init()

# Convert pandas DataFrame to H2O DataFrame
h2o_data = h2o.H2OFrame(data)

# Split data into training, validation, and test sets
train, valid, test = h2o_data.split_frame([0.7, 0.15])

# Display a summary of the split
print("Training set size:", train.shape[0])
print("Validation set size:", valid.shape[0])
print("Test set size:", test.shape[0])

# Shutdown H2O
h2o.shutdown()

# 3. Initialize H2O and Print Rapids Expression:

# Initialize H2O
h2o.init()

# Convert pandas DataFrames to H2O Frames
train_h2o = h2o.H2OFrame(train)
print("Training columns:", train_h2o.col_names)

valid_h2o = h2o.H2OFrame(valid)
print("Validation columns:", valid_h2o.col_names)
test_h2o = h2o.H2OFrame(test)

# Print Rapids expression for training frame
train_rapids_expr = train_h2o.as_rapids()
print("Rapids expression for training frame:", train_rapids_expr)
