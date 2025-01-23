#importing the libraries
import numpy as np
import pickle
import streamlit as st
import requests

# Function to download the model from URL and save it using pickle
def download_and_save_model(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('model.sav', 'wb') as f:
            f.write(response.content)
        st.write("Model saved as model.sav!")
    else:
        st.error(f"Error downloading the model: {response.status_code}")

# Load the model using pickle
def load_model():
    try:
        with open('model.sav', 'rb') as f:
            model = pickle.load(f)  # Load the actual model object
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# URL to your model (make sure the URL points to raw binary content)
url = 'https://github.com/Jess-chege/breast_cancer/blob/main/model.sav?raw=true'

# Download and save the model
download_and_save_model(url)

# Load the model
loaded_model = load_model()

# Function for breast cancer prediction
def breast_cancer_prediction(input_data):
    if loaded_model is None:
        return "Error loading model"
    
    input_data_as_numpy_array = np.array(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Make prediction
    try:
        prediction = loaded_model.predict(input_data_reshaped)
        if prediction[0] == 0:
            return "The person does not have breast cancer."
        else:
            return "The person has breast cancer."
    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return "Prediction error"

# Streamlit interface
def main():
    st.title("Breast Cancer Prediction Using Logistic Regression")
    
    # Getting the input data from the user
    mean_radius_input = st.text_input("Enter the patient's mean_radius:")
    mean_texture_input = st.text_input("Enter the patient's mean_texture:")
    mean_perimeter_input = st.text_input("Enter the patient's mean_perimeter:")
    mean_area_input = st.text_input("Enter the patient's mean_area:")
    mean_smoothness_input = st.text_input("Enter the patient's mean_smoothness:")
    
    # Convert inputs to numeric
    try:
        mean_radius = float(mean_radius_input)
        mean_texture = float(mean_texture_input)
        mean_perimeter = float(mean_perimeter_input)
        mean_area = float(mean_area_input)
        mean_smoothness = float(mean_smoothness_input)
    except ValueError:
        st.error("Please enter valid numeric values.")
        return

    # Create a list of input data
    input_data = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]
    
    # Prediction button
    if st.button("PREDICT"):
        diagnosis = breast_cancer_prediction(input_data)
        st.success(diagnosis)

if __name__ == '__main__':
    main()




    
    
    
    
    
    
    
    
    
    
    
