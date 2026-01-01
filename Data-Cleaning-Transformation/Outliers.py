import pandas as pd
# Load dataset
train = pd.read_csv("train.csv")
print("DATA TRAIN")
print(train.head())

# Memeriksa jumlah nilai yang hilang di setiap kolom
missing_values = train.isnull().sum()
missing_values[missing_values > 0]