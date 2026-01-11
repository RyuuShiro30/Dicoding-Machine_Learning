# ===============================
# 1. Import library
# ===============================
import pandas as pd
from sklearn.model_selection import train_test_split

# ===============================
# 2. Membuat contoh dataset
# ===============================
data = {
    'LotArea': [8450, 9600, 11250, 9550, 14260],
    'OverallQual': [7, 6, 7, 7, 8],
    'YearBuilt': [2003, 1976, 2001, 1915, 2000],
    'SalePrice': [208500, 181500, 223500, 140000, 250000]
}

df_lencoder = pd.DataFrame(data)

print("Dataset awal:")
print(df_lencoder)

# ===============================
# 3. Memisahkan fitur (X) dan target (y)
# ===============================
X = df_lencoder.drop('SalePrice', axis=1)
y = df_lencoder['SalePrice']

print("\nFitur (X):")
print(X)

print("\nTarget (y):")
print(y)

# ===============================
# 4. Data Splitting (Train & Test)
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% data testing
    random_state=42     # supaya hasil konsisten
)

# ===============================
# 5. Menampilkan hasil split
# ===============================
print("\nUkuran Data:")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)
print("y_train:", y_train.shape)
print("y_test :", y_test.shape)

print("\nData Training (X_train):")
print(X_train)

print("\nData Testing (X_test):")
print(X_test)
