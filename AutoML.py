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


# 3. Initialize H2O and Start AutoML:

# Initialize H2O
h2o.init()

# Convert pandas DataFrames to H2O Frames
train_h2o = h2o.H2OFrame(train)
valid_h2o = h2o.H2OFrame(valid)
test_h2o = h2o.H2OFrame(test)

# Priting Column Names
print("Training columns:", train_h2o.col_names)
print("Validation columns:", valid_h2o.col_names)

# # Identify the target column
# y = "cost"

# # Run AutoML with specified metrics and time constraints
# aml = H2OAutoML(max_runtime_secs=3600, seed=1)
# aml.train(y=y, training_frame=train_h2o, validation_frame=valid_h2o)



