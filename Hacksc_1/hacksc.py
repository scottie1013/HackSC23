

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression

# Load the trained model
# model = pickle.load('/Users/Utkarsha_1/Documents/heyy/svm.pkl')
import pickle

# Open the file in binary read mode
with open('C:/Users/Aditee/OneDrive/Documents/GitHub/Hacksc_1/svm.pkl', 'rb') as file:
    model = pickle.load(file)


# Define the data preprocessing function
def preprocess_data(age, menopause, tumer_size, inv_nodes, node_caps, irradiate):
    # Convert categorical variables to numericals representations
    menopause_mapping = {'premeno': 0, 'ge40': 1, 'lt40': 2}
    irradiate_mapping = {'no': 0, 'yes': 1}
    node_caps_mapping = {'no': 0, 'yes': 1}
    menopause = menopause_mapping[menopause]
    irradiate = irradiate_mapping[irradiate]
    node_caps = node_caps_mapping[node_caps]

    # Standardize numerical variables
    data = np.array([age, menopause, tumer_size, inv_nodes, node_caps, irradiate]).reshape(1, -1)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

# Create the Streamlit app
st.title('Breast Cancer Reccurence Prediction')

# Collect user input for the breast cancer parameters
age = st.number_input('Age', value=0, step=1, format="%d")
st.text('"10-19": 1, "20-29": 2, "30-39": 3, "40-49": 4, "50-59": 5, "60-69": 6, "70-79": 7, "80-89": 8, "90-99": 9')
menopause = st.selectbox('Menopause Status', ['premeno', 'ge40', 'lt40'])
tumer_size = st.number_input('Tumor Size', value=0, step=1, format="%d")
st.text('"0-4": 0, "5-9": 1, "10-14": 2, "15-19": 3, "20-24": 4, "25-29": 5, "30-34": 6, "35-39": 7, "40-44": 8, "45-49": 9, "50-54": 10, "55-59": 11')
inv_nodes = st.number_input('Number of Invasive Nodes', value=0, step=1, format="%d")
node_caps = st.selectbox('Node Caps', ['no', 'yes'])
irradiate = st.selectbox('Irradiation Therapy', ['no', 'yes'])


if st.button('Submit'):
    # Preprocess the user input data
    data = preprocess_data(age, menopause, tumer_size, inv_nodes, node_caps, irradiate)

    # Make a prediction using the trained model
    prediction = model.predict(data)

    # Display the prediction result
    if prediction == 0:
        result = "No Recurrence"
    else:
        result = "Recurrence"

    # Show the prediction result
    st.write(f'Prediction: {result}')


