import streamlit as st
import pandas as pd

df = pd.read_csv('D:\Startup_dashboard\Data\processed\cleaned_startup_data.csv')
df_by_investor = pd.read_csv('D:\Startup_dashboard\Data\processed\startup_investor_data.csv')

#Making sidebar
st.sidebar.title('Indian Startup Funding Analysis')

option = st.sidebar.selectbox("Select one", ['Overall Analysis','Startup Analysis','Investor Analysis'])

if option ==  'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup Analysis':
    st.sidebar.selectbox('Select startup', sorted(df['StartUp'].unique().tolist()))
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('Select Investor', sorted(df_by_investor['Investors'].unique().tolist())git remote -v)
    st.title('Investor Analysis')






