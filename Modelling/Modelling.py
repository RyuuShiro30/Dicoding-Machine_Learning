# =====================================
# 1. IMPORT LIBRARY
# =====================================
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lars
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# =====================================
# 2. LOAD DATASET CSV
# =====================================
# Pastikan file dataset_regresi.csv
# berada di folder yang sama dengan file Python / Notebook

df = pd.read_csv("dataset_regresi.csv")

# Cek 5 data teratas
print("Preview Data:")
print(df.head())


# =====================================
# 3. PISAHKAN FITUR & TARGET
# =====================================
X = df.drop(columns=['Target'])
y = df['Target']


# =====================================
# 4. SPLIT DATA TRAIN & TEST
# =====================================
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =====================================
# 5. MEMBUAT & MELATIH MODEL LARS
# =====================================
lars = Lars()
lars.fit(x_train, y_train)


# =====================================
# 6. PREDIKSI DATA TEST
# =====================================
pred_lars = lars.predict(x_test)


# =====================================
# 7. EVALUASI MODEL
# =====================================
mae_lars = mean_absolute_error(y_test, pred_lars)
mse_lars = mean_squared_error(y_test, pred_lars)
r2_lars = r2_score(y_test, pred_lars)


# =====================================
# 8. SIMPAN HASIL EVALUASI KE DATAFRAME
# =====================================
data = {
    'MAE': [mae_lars],
    'MSE': [mse_lars],
    'R2': [r2_lars]
}

df_results = pd.DataFrame(data, index=['LARS'])

print("\nHasil Evaluasi Model:")
print(df_results)
