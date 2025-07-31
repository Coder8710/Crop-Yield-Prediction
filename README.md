# 🌾 Crop Yield Prediction System

Predict crop yield based on environmental and agricultural parameters using a **CatBoost Machine Learning model**.  

🔗 **Project Website**: [Crop Yield Prediction App](https://crop-yield-prediction-jjyapppp2ytilbpmenuu9tsz.streamlit.app/)  
📊 **Dataset**: [Agriculture Crop Yield Dataset on Kaggle](https://www.kaggle.com/datasets/samuelotiattakorah/agriculture-crop-yield)

---

## 📖 Project Description

This project predicts **crop yield (tons/hectare)** using input features like:

- 🌍 Region  
- 🪨 Soil Type  
- 🌱 Crop Type  
- 🌧 Rainfall (mm)  
- 🌡 Temperature (°C)  
- 🧪 Fertilizer Usage  
- 💧 Irrigation Usage  
- ⛅ Weather Conditions  
- 📅 Days to Harvest  

It uses **CatBoost**, a powerful gradient boosting algorithm, to provide accurate yield predictions.

---

## 📂 Repository Contents

This repository contains:

1. **`app.py`** – The Streamlit web application.  
2. **`requirements.txt`** – Python dependencies for the project.  
3. **`crop_yield_catboost_gpu.cbm`** – Trained CatBoost model (original `.cbm` format).  
4. **`crop_yield_model.pkl`** – Pickle version of the trained model (for Streamlit deployment).  
5. **Jupyter Notebook / Python training code** – For training the CatBoost model.  

✅ This repo contains **both the training code** and the **trained model files**.

---

## 🧠 Model Used

- **Algorithm**: [CatBoost Regressor](https://catboost.ai/)  
- **Reason for Selection**: Handles categorical features efficiently, provides high accuracy, and works well with tabular agricultural data.  
- **Training Steps**:
  1. Preprocessed the Kaggle crop yield dataset.
  2. Encoded categorical variables.
  3. Trained a **CatBoostRegressor** with GPU support for faster training.
  4. Saved the model in both `.cbm` and `.pkl` formats.

---

## 🚀 How to Run Locally

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/crop-yield-prediction.git
cd crop-yield-prediction
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**:

```bash
streamlit run app.py
```

The app will start locally, and a browser window will open automatically.

---

## 🌐 How to Use the Web App

1. Open the [web app](https://crop-yield-prediction-jjyapppp2ytilbpmenuu9tsz.streamlit.app/).  
2. Enter the required **crop and environmental details**.  
3. Click **“Predict Yield”** to get the expected crop yield in **tons/hectare**.  
4. View the **Prediction History** to check your last predictions.  
