# 🌾 Crop Yield Prediction System

A **machine learning-based web application** to predict **crop yield (tons/hectare)** based on environmental and crop-specific factors.  
This project allows farmers, researchers, and agricultural enthusiasts to **estimate potential yield** and make **data-driven decisions**.

---

## 🔗 Live Demo
Try the live app here: **[🌱 Crop Yield Prediction Website](https://crop-yield-prediction-jjyapppp2ytilbpmenuu9tsz.streamlit.app/)**

---

## 📖 Project Description
Efficient crop yield prediction helps in:

- **Optimizing resource usage** (water, fertilizer, and manpower).  
- **Planning harvest cycles** to maximize output.  
- **Mitigating risks** related to unfavorable weather conditions.  

This web app takes in **environmental factors** like rainfall, temperature, soil type, weather conditions, irrigation, and fertilizer usage, then predicts the **expected yield** for a selected crop.

---

## 📊 Dataset
We trained our model using the **Agriculture Crop Yield Dataset** from Kaggle:

🔗 **[Agriculture Crop Yield Dataset](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)**

**Dataset Features:**
- Region (North, South, East, West)
- Soil Type (Clay, Sandy, Loam, Silt, Peaty, Chalky)
- Crop (Wheat, Rice, Maize, Barley, Soybean, Cotton)
- Rainfall (mm)
- Temperature (°C)
- Fertilizer Used (True/False)
- Irrigation Used (True/False)
- Weather Condition (Sunny, Rainy, Cloudy)
- Days to Harvest (integer)

**Target Variable:** Crop Yield (tons/hectare)

---

## 🤖 Machine Learning Model

- **Model Used:** [CatBoost Regressor](https://catboost.ai/)  
- **Why CatBoost?**
  - Handles **categorical features** without extra encoding.
  - Performs well on **tabular datasets**.
  - GPU/CPU compatible and efficient.  

**Steps followed:**
1. Preprocessed the dataset (handled categorical and numerical features).  
2. Split into **train/test sets**.  
3. Trained a **CatBoost Regressor** with optimized parameters.  
4. Saved the model as a **pickle (.pkl)** file for deployment.  

**Additional Info:**
- This repository also **includes the CatBoost training notebook**: `crop_yield_prediction.ipynb`  
- The **trained `.cbm` model** is included for anyone who wants to load and use the original CatBoost model directly.  
- A helper script **`cbm_to_pkl.py`** is provided to **convert `.cbm` models into `.pkl` format** for easier deployment on Streamlit Cloud.

---

## 🚀 How to Use the Project

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/crop-yield-prediction.git
cd crop-yield-prediction
