import numpy as np
from sklearn.linear_model import Lars
import joblib

# Dummy dataset
X = np.array([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
])

y = np.array([10, 15, 20, 25])

# Train model
model = Lars()
model.fit(X, y)

# Save model
joblib.dump(model, "lars_model.joblib")

print("Model berhasil dibuat!")
