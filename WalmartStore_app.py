
import streamlit as st
import joblib
import pandas as pd

# Load the data file
data = pd.read_csv("streamlit_data.csv")

# Load the preprocessor and model
preprocessor = joblib.load('preprocessor.pkl')
poly = joblib.load('poly.pkl')
lin_reg = joblib.load('linear_regression_model.pkl')

# Streamlit app layout
st.title('Weekly Sales Prediction')

# User input using sliders
store = st.selectbox('Store', data['Store'].unique())
holidays = st.selectbox('Holidays', data['Holidays'].unique())
week = st.selectbox('Week', data['Week'].unique())
month_name = st.selectbox('Month Name', data['Month_Name'].unique())
season = st.selectbox('Season', data['Season'].unique())
temperature = st.slider('Temperature', min_value=data['Temperature'].min(), max_value=data['Temperature'].max())
cpi = st.slider('CPI', min_value=data['CPI'].min(), max_value=data['CPI'].max())
unemployment = st.slider('Unemployment', min_value=data['Unemployment'].min(), max_value=data['Unemployment'].max())

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'Store': [store],
    'Holidays': [holidays],
    'Temperature': [temperature],
    'CPI': [cpi],
    'Unemployment': [unemployment],
    'Week': [week],
    'Month_Name': [month_name],
    'Season': [season]
})

# Transform the data into a DataFrame
features = pd.DataFrame(input_data, index=[0])  

# Predict button
if st.button('Predict Weekly Sales'):
    # Preprocess the input data
    transformed_data = preprocessor.transform(features)
    
    transformed_data_poly = poly.transform(transformed_data)

    # Make predictions
    prediction = lin_reg.predict(transformed_data_poly)
    
    # Display the prediction
    st.success(f'Predicted Weekly Sales: {prediction[0]:.2f}')
