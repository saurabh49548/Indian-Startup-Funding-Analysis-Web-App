import streamlit as st
import pandas as pd

df = pd.read_csv('startup_funding.csv')

#Making sidebar
st.sidebar.title('Indian Startup Funding Analysis')

option = st.sidebar.selectbox("Select one", ['Overall Analysis','Startup Analysis','Investor Analysis'])

if option ==  'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup Analysis':
    st.sidebar.selectbox('Select startup', ['Byjus', 'Ola', 'Flipkart'])
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('Select Investor', ['Person_1','Person_2','Person_3','Person_4','Person_5'])
    st.title('Investor Analysis')






