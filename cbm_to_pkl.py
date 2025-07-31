import pickle
from catboost import CatBoostRegressor

# Load the CatBoost model from .cbm file
cbm_model = CatBoostRegressor()
cbm_model.load_model("crop_yield_catboost_gpu.cbm")

# Save the model as .pkl using pickle
with open("crop_yield_model.pkl", "wb") as f:
    pickle.dump(cbm_model, f)

print("Model successfully converted to crop_yield_model.pkl")
