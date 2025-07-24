# House Price Prediction (Melbourne)

A machine learning project to predict housing prices in Melbourne using data from Kaggle and a Random Forest regression model. Built in Python with Streamlit for a user-friendly web interface.

##  Features

- Predict house prices based on user inputs
- Cleaned and preprocessed real-world housing data
- Compared Linear Regression and Random Forest models
- Tuned model using GridSearchCV
- Deployed as an interactive web app with Streamlit

## Model Performance

| Model              | MAE       | RMSE      | R² Score |
|--------------------|-----------|-----------|----------|
| Linear Regression  | 239,889   | 1,271,484 | 0.67     |
| Random Forest      | 192,772   | 307,312   | 0.76     |
| Tuned RF (Final)   | 191,711   | 305,005   | 0.76     |

## Folder Structure

- `notebooks/` → EDA + modeling
- `data/` → Melbourne dataset
- `app.py` → Streamlit interface
- `model_rf.pkl` → Final trained model
- `requirements.txt` → Python packages

## Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
