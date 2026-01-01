import pandas as pd

# Load data
df_lencoder = pd.read_csv("ipk.csv")

# Melihat 5 data teratas
print(df_lencoder.head())

# Total baris data
total_rows = len(df_lencoder)

# Hitung missing values per kolom
missing_summary = (
    df_lencoder
    .isnull()
    .sum()
    .reset_index()
)

# Rename kolom
missing_summary.columns = ['Kolom', 'Missing Values']

# Hitung persentase missing
missing_summary['Percentage (%)'] = (
    missing_summary['Missing Values'] / total_rows * 100
).round(2)

# Ambil hanya kolom yang memiliki missing value
missing_summary = missing_summary[missing_summary['Missing Values'] > 0]

# Urutkan dari yang paling banyak missing
missing_summary = missing_summary.sort_values(
    by='Missing Values',
    ascending=False
)

print(missing_summary)
