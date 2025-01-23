#importing the libraries

import numpy as np
import pickle #load the model
import streamlit as st
import pandas as pd
import requests

#Loading model from github
url = 'https://github.com/Jess-chege/breast_cancer/blob/main/model.sav'

loaded_model = requests.get(url)
 

with open('log_reg.bin', 'wb') as f:
    pickle.dump(loaded_model, f)
    
#load model 
with open('log_reg.bin', 'rb') as f:
          loaded_model =pickle.load(f)
        
def breast_cancer_prediction(input_data):
    
    input_data_as_numpy_array(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    #instead of model we use loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    
    
    if prediction [0] == 0:
        return"The person does not have breast cancer"
    else:
        return"The person has breast cancer"
        
#streamlit library  to create a user interface
def main():
    
    st.title("Breast Cancer Prediction Machine Learning Model")
    
    #getting the input data from user
    mean_radius_input = input("Enter the patients' mean_radius: ")
    mean_texture_input = input("Enter the patients' mean_texture")
    mean_perimeter_input= input("Enter the patients' mean_perimeter")
    mean_area_input = input("Enter the patients' mean_area")
    mean_smoothness_input= input("Enter the patients' mean_smoothness")
    
    
    
#numeric conversions

    mean_radius = pd.to_numeric(mean_radius_input, errors='coerce')
    mean_texture = pd.to_numeric(mean_texture_input, errors='coerce')
    mean_perimeter= pd.to_numeric(mean_perimeter_input, errors='coerce')
    mean_area = pd.to_numeric(mean_area_input, errors='coerce')
    mean_smoothness= pd.to_numeric(mean_smoothness_input, errors='coerce')
   

    diagnosis = ''
    
    #creating a prediction button
    if st.button("PREDICT"):
        diagnosis = breast_cancer_disease([mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness])
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()

    
    
    
    
    
    if prediction [0] == 0:
        return"The person does not have breast cancer"
    else:
        return"The person has breast cancer"
        
#streamlit library  to create a user interface
def main():
    
    st.title("Breast Cancer Prediction Machine Learning Model")
    
    #getting the input data from user
    mean_radius_input = input("Enter the patients' mean_radius: ")
    mean_texture = input("Enter the patients' mean_texture")
    mean_perimeter= input("Enter the patients' mean_perimeter")
    mean_area = input("Enter the patients' mean_area")
    mean_smoothness= input("Enter the patients' mean_smoothness")
    
    
    
#numeric conversions

    mean_radius = pd.to_numeric(mean_radius_input, errors='coerce')
    mean_texture = pd.to_numeric(mean_texture_input, errors='coerce')
    mean_perimeter= pd.to_numeric(mean_perimeter_input, errors='coerce')
    mean_area = pd.to_numeric(mean_area_input, errors='coerce')
    mean_smoothness= pd.to_numeric(mean_smoothness_input, errors='coerce')
   

    diagnosis = ''
    
    #creating a prediction button
    if st.button("PREDICT"):
        diagnosis = breast_cancer_disease([mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness])
    st.success(diagnosis)
    
if __name__ =='__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    
