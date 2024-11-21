#importing libraries
import streamlit as st
import joblib
import numpy as np

# loading the pre-trained model
model = joblib.load('breast_cancer_classification_model.pkl')

#Title for the app
st.title('Breast Cancer Type Classification')

#User input fields
radius_mean = st.number_input('Enter Radius_mean', min_value = 0.0)
texture_mean = st.number_input('Enter Texture_mean', min_value = 0.0)
perimeter_mean = st.number_input('Enter Perimeter_mean', min_value = 0.0)
area_mean = st.number_input('Enter Area_mean', min_value = 0.0)
smoothness_mean = st.number_input('Enter Smoothness_mean', min_value = 0.0)
compactness_mean = st.number_input('Enter Compactness_mean', min_value = 0.0)
concavity_mean = st.number_input('Enter concavity_mean', min_value = 0.0)
concave_points_mean = st.number_input('Enter Concave_points_mean', min_value = 0.0)
symmetry_mean = st.number_input('Enter symmetry_mean', min_value = 0.0)
fractal_dimension_mean = st.number_input('Enter Fractal_dimension_mean', min_value = 0.0)
radius_se = st.number_input('Enter Radius_se', min_value = 0.0)
texture_se = st.number_input('Enter Texture_se', min_value = 0.0)
perimeter_se = st.number_input('Enter Perimeter_se', min_value = 0.0)
area_se = st.number_input('Enter Area_se', min_value = 0.0)
smoothness_se = st.number_input('Enter Smoothness_se', min_value = 0.0)
compactness_se = st.number_input('Enter Compactness_se', min_value = 0.0)
concavity_se = st.number_input('Enter Concavity_se', min_value = 0.0)
concave_points_se = st.number_input('Enter Concave_points_se', min_value = 0.0)
symmetry_se = st.number_input('Enter Symmetry_se', min_value = 0.0)
fractal_dimension_se = st.number_input('Enter Fractal_dimension_se', min_value = 0.0)
radius_worst = st.number_input('Enter Radius_worst', min_value = 0.0)
texture_worst = st.number_input('Enter Texture_worst', min_value = 0.0)
perimeter_worst = st.number_input('Enter Perimeter_worst', min_value = 0.0)
area_worst = st.number_input('Enter Area_worst', min_value = 0.0)
smoothness_worst = st.number_input('Enter Smoothness_worst', min_value = 0.0)
compactness_worst = st.number_input('Enter Compactness_worst', min_value = 0.0)
concavity_worst = st.number_input('Enter Concavity_worst', min_value = 0.0)
concave_points_worst = st.number_input('Enter Concave_points_worst', min_value = 0.0)
symmetry_worst = st.number_input('Enter Symmetry_worst', min_value = 0.0)
fractal_dimension_worst = st.number_input('Enter Fractal_dimension_worst', min_value = 0.0)


# putting the user's input as an array
user_input = np.array([[radius_mean, texture_mean, perimeter_mean,
       area_mean, smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]])

#making the prediction
if st.button('Predict'):
    prediction = model.predict(user_input)
    if prediction == 0:
        st.write('The Breast Cancer is Benign')
    else:
        st.write('The Breast Cancer is Malignant')