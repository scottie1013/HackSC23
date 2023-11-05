
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
with open('C:/Users/Aditee/OneDrive/Documents/GitHub/Hacksc_1/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)


# Define the data preprocessing function
def preprocess_data(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
    # Convert categorical variables to numericals representations
    # menopause_mapping = {'premeno': 0, 'ge40': 1, 'lt40': 2}
    # irradiate_mapping = {'no': 0, 'yes': 1}
    # node_caps_mapping = {'no': 0, 'yes': 1}
    # menopause = menopause_mapping[menopause]
    # irradiate = irradiate_mapping[irradiate]
    # node_caps = node_caps_mapping[node_caps]
    
    

    # Standardize numerical variables
    data = np.array([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst,concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]).reshape(1, -1)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

# Create the Streamlit app
st.title('Breast Cancer Reccurence Prediction')

# Collect user input for the breast cancer parameters
radius_mean=st.number_input('radius-mean')
texture_mean=st.number_input('texture_mean')
perimeter_mean=st.number_input('perimeter_mean')
area_mean=st.number_input('area_mean')
smoothness_mean=st.number_input('smoothness_mean')
compactness_mean=st.number_input('compactness_mean')
concavity_mean=st.number_input('concavity_mean')
concave_points_mean=st.number_input('concave_points_mean')
symmetry_mean=st.number_input('symmetry_mean')
fractal_dimension_mean=st.number_input('fractal_dimension_mean')
radius_se=st.number_input('radius_se')
texture_se=st.number_input('texture_se')
perimeter_se=st.number_input('perimeter_se')
area_se=st.number_input('area_se')
smoothness_se=st.number_input('smoothness_se')
compactness_se=st.number_input('compactness_se')
concavity_se=st.number_input('concavity_se')
concave_points_se=st.number_input('concave_points_se')
symmetry_se=st.number_input('symmetry_se')
fractal_dimension_se=st.number_input('fractal_dimension_s')
radius_worst=st.number_input('radius_worst')
texture_worst=st.number_input('texture_worst')
perimeter_worst=st.number_input('perimeter_worst')
area_worst=st.number_input('area_worstn')
smoothness_worst=st.number_input('smoothness_worst')
compactness_worst=st.number_input('compactness_worst')
concavity_worst=st.number_input('concavity_worst')
concave_points_worst=st.number_input('concave_points_worst')
symmetry_worst=st.number_input('symmetry_worst')
fractal_dimension_worst=st.number_input('fractal_dimension_worstn')


if st.button('Submit'):
    # Preprocess the user input data
    data = preprocess_data(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean,fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se,fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst,smoothness_worst, compactness_worst,concavity_worst, concave_points_worst,symmetry_worst, fractal_dimension_worst)

    # Make a prediction using the trained model
    prediction = model.predict(data)

    # Display the prediction result
    if prediction == 0:
        result = "Benign"
    else:
        result = "Malign"

    # Show the prediction result
    st.write(f'Prediction: {result}')


