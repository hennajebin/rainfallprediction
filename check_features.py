import joblib

model = joblib.load("rainfallprediction4.joblib")

print(model.feature_names_in_)