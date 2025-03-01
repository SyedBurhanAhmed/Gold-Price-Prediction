import joblib
import pandas as pd
import streamlit as st

# Load the pre-trained model
model = joblib.load('linear_regression_model.pkl')

# Conversion factors
conversion_factors = {
    'ounce': 1,  # No conversion needed for ounce
    'troy ounce': 1.09714,  # 1 ounce = 1.09714 troy ounce
    'tola': 11.6638,  # 1 ounce = 11.6638 tola
    'gram': 31.1035,  # 1 ounce = 31.1035 grams
}

# Streamlit App
st.title('Gold Price Prediction in Pakistan')

# Input fields for features
global_gold_price_usd = st.number_input('Global Gold Price (USD)', min_value=0.0)
usd_to_pkr = st.number_input('USD to PKR Exchange Rate', min_value=0.0)
petrol_price_pkr = st.number_input('Petrol Price in Pakistan (PKR)', min_value=0.0)

# Dropdown for selecting the unit of measurement
unit = st.selectbox('Select Unit for Gold Price', ['ounce', 'troy ounce', 'tola', 'gram'])

# Predict button
if st.button('Predict'):
    # Prepare input data for prediction
    input_data = pd.DataFrame({
        'global_gold_price_usd': [global_gold_price_usd],
        'usd_to_pkr': [usd_to_pkr],
        'petrol_price_pkr': [petrol_price_pkr]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Convert the predicted price to the selected unit
    predicted_price_pkr = prediction[0]
    converted_price = predicted_price_pkr * conversion_factors[unit]

    # Display result
    st.write(f'Predicted Gold Price in Pakistan (PKR per ounce): {predicted_price_pkr:.2f}')
    st.write(f'Converted Gold Price in {unit}: {converted_price:.2f}')
