import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate random data for the dataset
age = np.random.randint(18, 65, size=10000)
sex = np.random.choice(['male', 'female'], size=10000)
bmi = np.random.uniform(18.5, 40, size=10000)
children = np.random.randint(0, 5, size=10000)
smoker = np.random.choice(['yes', 'no'], size=10000)
region = np.random.choice(['northeast', 'southeast', 'southwest', 'northwest'], size=10000)
income = np.random.randint(30000, 80000, size=10000)
cost = np.random.uniform(80, 250, size=10000)

# Create a DataFrame
df = pd.DataFrame({
    'age': age,
    'sex': sex,
    'bmi': bmi,
    'children': children,
    'smoker': smoker,
    'region': region,
    'income': income,
    'cost': cost
})

# Save the DataFrame to a CSV file
df.to_csv('life_insurance_data.csv', index=False)
