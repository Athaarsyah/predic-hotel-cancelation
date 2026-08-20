import sys

import joblib
import numpy as np
import streamlit as st
from sklearn._loss import loss as sklearn_loss

sys.modules.setdefault("_loss", sklearn_loss)

model = joblib.load("gb_booking_model.pkl")

st.title("Hotel Booking Cancellation Predictor")

st.divider()

st.write("Enter booking detail to predict cancellation.")

lead_time = st.slider('Lead Time', 0, 500, 50)
avg_price = st.number_input('Averange Price Per Room', 0.0, 500.0, 100.0)
special_requests = st.slider('Number of special requests', 0,5,1 )
total_guests = st.slider('Total guests', 1 , 10, 2)
total_nights = st.slider('Total nights', 1 , 30, 3)
repeated_guest = st.selectbox('Repeared guest', [0, 1])

if st.button('Predict'):
  input_data = np.array([[
    lead_time,
    avg_price,
    special_requests,
    total_guests,
    total_nights,
    repeated_guest
  ]])

  prediction = model.predict(input_data)[0]
  prob = model.predict_proba(input_data)[0][1]

  if prediction == 1:
    st.success(f"Prediction: Not Canceled (Probability: {prob:.2f})")
  else:
    st.error(f"Prediction: Canceled (Probability: {1- prob:.2f})")