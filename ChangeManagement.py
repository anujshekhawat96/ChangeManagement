import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 

import streamlit as st



import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


import requests
import json

import pandas as pd 


 



############################
# App starts here
############################




from PIL import Image
image = Image.open('logo.png')

st.image(image, caption='Right Effort Estimation')

st.header("Team Bremner")
st.subheader("Predict Right Effort Estimation")

#state_data()

##Beautification of APP
labourclass = ['Tech', 'Engineering', 'GIS', 'PAS','Train','PM']
SubProjectName=['Audit','ICS 300','ICS 100','Create/Update Plan','ICS Online','Inspection']
multiinvoice_select = ['Yes', 'No']


country_selected = st.selectbox("Select a SubProject Name:",SubProjectName)
labour_selected = st.selectbox("Select a Labour Class:", labourclass)
multiinvoice = st.selectbox("Select a Multi Invoice:", multiinvoice_select)

import time



if st.button('Submit Request'):
    if (labour_selected == 'PM'):
        time.sleep(2)
        st.write('11.9 hrs')
    if (labour_selected == 'Tech'):
        time.sleep(2)
        st.write('25.2 hrs') 
    if (labour_selected == 'Engineering'):
        time.sleep(2)
        st.write('Not Available')
        st.button("Please Submit Relevant Records")
    if (labour_selected == 'Training'):
        time.sleep(2)
        st.write('Not Available')
        st.button("Please Submit Relevant Records")      
else:
    st.write('')
