# importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings
from PIL import Image

# To ignore warnings that are not useful 
warnings.filterwarnings('ignore') 
phsh_model = pickle.load(open('phishing.pkl', 'rb'))
st.title('Phishing Website Detection')
# st.write('This web application is used to detect whether a website is a phishing website or not.')
st.write('Please enter the URL of the website to check if it is a phishing website or not.')
# Creating a text box for user input
input_url=st.text_input('Enter the URL of the website:')
image=['phishing_img.jpeg','safe.jpg']
def check_phishing(input_url):
    return phsh_model.predict([input_url])
if st.button('Check'):
    output=check_phishing(input_url)
    if output=='bad':
        st.markdown(f''' 
                        ⚠️☠️🚨:red[**This is a phishing website**]⚠️☠️🚨      ''')
        bottom_image = image[0]
        image = Image.open(bottom_image)
        new_image = image.resize((600, 400))
        st.image(new_image)
    else:
        st.markdown(f'''            
                        ✅✅✅ :green[**This is a safe website**] ✅✅✅        ''')
        st.image(image[1], output_format='jpg',width=300,use_column_width=True)
# st.write('The model used in this application is a Random Forest Classifier model which is trained on the Phishing Website dataset from UCI Machine Learning Repository.')

