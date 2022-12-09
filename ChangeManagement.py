import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 

import streamlit as st

from st_aggrid import AgGrid
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


import requests
import json

import pandas as pd 
from PIL import Image
#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')
from PIL import Image
image = Image.open('logo.png')

def state_data():
    city_list = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai']
    country_list=['India','Bangladesh','Pakistan','Nepal','Srilanka']
    country_selected = st.selectbox("Select a Country",country_list)
    state_selected = st.selectbox("Select a State:", city_list)
    
    treatment = ['Heart Surgery','Knee Surgery','Liver Transplant','Kidney Transplant','Other Surgeries']
    treatment_selected = st.selectbox("Select a Treatment Looking for:", treatment)
    List_hospital = ['Ganga Ram Hospital', 'LIBS', 'MAX Hospital','Medanta Hospital']
    Price = ['Rs.120000','Rs.300000','Rs.70000','Rs.120000']
    
    if(treatment_selected=='Heart Surgery'):
        lst = [['Ganga Ram Hospital', 'Rs.120,000','Dr. John','100','45','55'], ['LIBS', 'Rs.300,000','Dr. AS','150','100','50'],
       ['MAX Hospital', 'Rs.70,000', 'Dr. FK','200','190','10'], ['Medanta Hospital', 'Rs.100,000','Dr. Raun','500','250','250'],['Yashoda Hospital', 'Rs.100,000','Dr. Raun','500','250','250']]
        df_heart = pd.DataFrame(lst, columns =['Hospital Name', 'Cost', 'Doctor Name','Total Number of Beds','Occupied','Vacant'])
               
        
        AgGrid(df_heart)
    else:
        lst = [['Ortho', 'Rs.75000'], ['Dr Ortho', 'Rs.85000'],
            ['MAX Hospital', 'Rs.35000'], ['ABC Hospital', 'Rs.55000']]
        df_else = pd.DataFrame(lst, columns =['Hospital Name', 'Cost'])   
        st.dataframe(df_else)  




	
	

############################
# App starts here
############################
from PIL import Image



st.header("Team Bremner")
st.subheader("Find the Right Hours")

#state_data()

##Beautification of APP
labourclass = ['Tech', 'Engineering', 'GIS', 'PAS','Train','PM']
SubProjectName=['Audit','ICS 300','ICS 100','Create/Update Plan','ICS Online','Inspection']
multiinvoice_select = ['Yes', 'No']


country_selected = st.selectbox("Select a SubProject Name",SubProjectName)
state_selected = st.selectbox("Select a Labour Class:", labourclass)
multiinvoice = st.selectbox("Select a Multi Invoice:", multiinvoice_select)



if st.button('Submit Request'):
    if (labourclass == 'PM'):
        st.write('29.4 hrs')
    if (labourclass == 'Tech'):
        st.write('25.2 hrs') 
    
else:
    st.write('Not Available')