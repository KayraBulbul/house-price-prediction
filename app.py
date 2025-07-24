import streamlit as st
import numpy as np
import pandas as pd
import pickle

with open("model_rf.pkl", "rb") as f:
    data = pickle.load(f)
    model = data['model']
    model_columns = data['columns']

st.title("🏠 Melbourne House Price Predictor")
st.write("Enter property details to estimate the price:")

rooms = st.slider("Number of Rooms", 1, 10, 3)
bedroom2 = st.slider("Total Bedrooms", 1, 10, 3)
distance = st.slider("Distance to CBD (km)", 0, 50, 10)
bathroom = st.slider("Number of Bathrooms", 1, 5, 2)
car = st.slider("Number of Car Spots", 0, 5, 1)
landsize = st.number_input("Land Size (sqm)", min_value=0, max_value=10000, value=500)
type_u = st.selectbox("Is the property a Unit?", ["No", "Yes"]) == "Yes"
method_s = st.selectbox("Was it sold privately?", ["No", "Yes"]) == "Yes"

suburb_choice = st.selectbox("Suburb", ["Brighton", "Hampton", "Other"])
suburb_brighton = int(suburb_choice == "Brighton")
suburb_hampton = int(suburb_choice == "Hampton")

user_input = {
    'Bedroom2': bedroom2,
    'Suburb_Hampton': int(suburb_hampton),
    'Method_S': int(method_s),
    'Suburb_Brighton': int(suburb_brighton),
    'Car': car,
    'Bathroom': bathroom,
    'Type_u': int(type_u),
    'Landsize': landsize,
    'Rooms': rooms,
    'Distance': distance
}

input_df = pd.DataFrame([user_input])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

if st.button("Predict Price"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.0f}")
