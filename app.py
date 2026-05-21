
from matplotlib.pyplot import ylabel
from streamlit.elements import deck_gl_json_chart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Setting page layout
st.set_page_config(
    layout = 'wide',
    initial_sidebar_state = 'collapsed',
    page_title = "Indian Startup Funding Analysis",
    page_icon = "📊"
)

df = pd.read_csv('D:\Startup_dashboard\Data\processed\clean_startup_data.csv',parse_dates=['Date'])
df['Year']=df['Date'].dt.year   #Extracting year from Date column
df['Month']=df['Date'].dt.month #Extracting month from Date column

#Making sidebar
st.sidebar.title('Indian Startup Funding Analysis')

option = st.sidebar.selectbox("Select one", ['Overall Analysis','Startup Insights','Investor Insights'])

def load_overall_analysis():
        st.title('Startup Ecosystem Overview')

        col1,col2,col3,col4 = st.columns(4)

        #Total funding amount
        tot_amt = round(df['Amount'].sum())
        
        #Max amount infused in a startup or max ticket size
        max_amt = df.groupby('StartUp')['Amount'].max().sort_values(ascending=False).head(1).values[0]
        
        #Average Ticket Size
        avg_amt = round(df.groupby('StartUp')['Amount'].sum().mean(),2)
        
        #Number of Startups
        num_startups = df['StartUp'].nunique()

        with col1:
            #Total funding amount
            st.metric("Total Funding Amount",f"{tot_amt} Cr")

        with col2:
            #Max amount infused in a startup
            st.metric("Max Infused Amount",f"{max_amt} Cr")

        with col3:
            #Average per startup
            st.metric("Average Funding per Startup",f"{avg_amt} Cr")

        with col4:
            #Number of Startups
            st.metric("Number of Funded Startups",f"{num_startups}")

        #Amount of funding per quarter 
        st.subheader("Monthly Funding Analysis")
        selected_option = st.selectbox("Select Option",['Total Investment','Number of Startups Funded'])

        if selected_option == 'Total Investment':
            temp_df1= df.groupby(['Year','Month'])['Amount'].sum().reset_index()
            temp_df1['x-axis']= temp_df1['Month'].astype('str') + '-' + temp_df1['Year'].astype('str')

            fig,ax = plt.subplots(figsize=(12, 6))
            ax.plot(temp_df1['x-axis'],temp_df1['Amount'],marker='o')
            plt.xticks(temp_df1['x-axis'][::4],rotation = 45)
            plt.ylabel('Amount(in Crores)',fontsize = 12)
            plt.xlabel('Month',fontsize = 12)
            st.pyplot(fig)

        else:
            temp_df2 = df.groupby(['Year','Month'])['StartUp'].count().reset_index()
            temp_df2['x-axis'] = temp_df2['Month'].astype('str') + '-' + temp_df2['Year'].astype('str')

            fig1, ax1 = plt.subplots(figsize=(12, 6))
            ax1.plot(temp_df2['x-axis'],temp_df2['StartUp'],marker='o')
            plt.xticks(temp_df2['x-axis'][::4],rotation = 45)
            plt.ylabel('Number of Startups Funded',fontsize = 12)
            plt.xlabel('Month',fontsize = 12)
            st.pyplot(fig1)
        
        col5,col6 = st.columns(2)
        with col5:
            # Location wise funding analysis
            location_series = df.groupby('Location')['Amount'].sum().sort_values(ascending=False).head()
            st.subheader('Geographical Investment Distribution')
            fig2,ax2 = plt.subplots()
            ax2.bar(location_series.index,location_series.values)
            plt.title('Top Investment Locations',fontsize = 12)
            plt.ylabel('Amount(in Crores)',fontsize=12)
            plt.xlabel('Location',fontsize=12)
            st.pyplot(fig2)
        
        with col6:
            # Sector wise funding analysis
            st.subheader('Sector Wise Analysis')
            select_option = st.selectbox('Select Option',['Top Sectors by Investment Value','Top Sectors by Startup Count'])
            if select_option == 'Top Sectors by Investment Value':
                
                sector_series1 = df.groupby('Vertical')['Amount'].sum().sort_values(ascending = False).head()
                fig3,ax3 = plt.subplots()
                wedges, texts = ax3.pie(sector_series1)
                ax3.pie(sector_series1,autopct='%1.1f%%')
                ax3.legend(sector_series1.index,title="Sectors",loc="center left")
                ax3.legend(wedges,sector_series1.index,title="Sectors",loc="center left",bbox_to_anchor=(1, 0.5))
                plt.title('Top Funded Sectors (By Capital)',fontsize=12)
                st.pyplot(fig3)


        
        


def load_investor_details(investor):
    st.title(investor)
    
    #Load the recent 5 investments of the investor
    last_5 = df[df['Investors'].str.contains(investor)].head()[['Date','StartUp','Vertical','Location','Round','Amount']]
    st.subheader('Recent Investments')
    st.dataframe(last_5)
    
    col1,col2 = st.columns(2)
    with col1:
        #Biggest Investments
        big_series = df[df['Investors'].str.contains(investor)].groupby('StartUp')['Amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        plt.ylabel('Amount(in Crores)', fontsize =12)
        plt.xlabel('Startup', fontsize =12)
        plt.title('Biggest Investments', fontsize=12)
        st.pyplot(fig)
    
    with col2:
        #Sector Wise Investments
        sector_series= df[df['Investors'].str.contains(investor)].groupby('Vertical')['Amount'].sum().head()
        st.subheader('Top Investment Sectors')
        fig1, ax1 = plt.subplots()
        wedges, texts, autotexts = ax1.pie(sector_series.values,autopct='%1.1f%%')
        # Separate legend
        ax1.legend(wedges,sector_series.index,title="Sectors",loc="center left",bbox_to_anchor=(1, 0.5))
        plt.title('Sector Wise Investments')
        st.pyplot(fig1)
    
    col3,col4 = st.columns(2)
    with col3:
        #Stage wise analysis
        stage_series = df[df['Investors'].str.contains(investor)].groupby('Round')['Amount'].sum()
        st.subheader('Stage Wise Investments')
        fig3, ax3 = plt.subplots()
        wedges, texts = ax3.pie(stage_series)

        # Calculate percentages
        total = stage_series.sum()
        labels = [
            f"{label} ({value/total*100:.1f}%)"
            for label, value in zip(stage_series.index, stage_series)
        ]
        
        # Separate legend
        ax3.legend(wedges,labels,title="Stages",loc="center left",bbox_to_anchor=(1, 0.5))
        st.pyplot(fig3)
    
    with col4:
        city_series= df[df['Investors'].str.contains(investor)].groupby('Location')['Amount'].sum()
        st.subheader('Top Investment Cities')
        fig4,ax4 = plt.subplots()
        wedges,texts= ax4.pie(city_series)

        # Calculate percentages
        total_city = city_series.sum()
        labels=[
            f"{label} ({value/total_city*100:.1f}%)"
            for label,value in zip(city_series.index,city_series)
        ]

        #Seprate legend
        ax4.legend(wedges,labels,title="Cities",loc="center left",bbox_to_anchor=(1, 0.5))
        plt.title('City Wise Investments')
        st.pyplot(fig4)
    
    

    #Investment trend over Time
    yearly_investment = df[df['Investors'].str.contains(investor)].groupby('Year')['Amount'].sum().reset_index()
    st.subheader('Investment trend over Time')

    #Line plots to show YOY trend
    fig5,ax5 = plt.subplots(figsize=(12, 4))
    ax5.plot(yearly_investment['Year'],yearly_investment['Amount'],markersize=10,linestyle='-')
    plt.ylabel('Amount(in Crores)',fontsize=12)
    plt.xlabel('Year',fontsize=12)
    plt.title('Year On Year Investments',fontsize=12)
    plt.xticks(yearly_investment['Year'])
    st.pyplot(fig5)
    

#Overall Analysis
if option ==  'Overall Analysis':
        load_overall_analysis()


#Startup Analysis
elif option == 'Startup Insights':
    st.sidebar.selectbox('Select startup', sorted(df['StartUp'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    st.title('Startup Insights')

#Investor Analysis
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['Investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor details')
    st.title('Investor Insights')

    if btn2:
        load_investor_details(selected_investor)
        
    






