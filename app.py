
from matplotlib.pyplot import ylabel
from streamlit.elements import deck_gl_json_chart
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker

#Setting page layout
st.set_page_config(
    layout = 'wide',
    initial_sidebar_state = 'collapsed',
    page_title = "Indian Startup Funding Analysis",
    page_icon = "📊"
)

df = pd.read_csv('D:\Startup_dashboard\Data\processed\startup_data.csv',parse_dates=['Date'])
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
            st.subheader('Sector-wise Investment Analysis')
            select_option = st.selectbox('Select Option',['Top Sectors by Investment Value','Top Sectors by Startup Count'])
            if select_option == 'Top Sectors by Investment Value':
                
                sector_series1 = df.groupby('Vertical')['Amount'].sum().sort_values(ascending = False).head()
                fig3,ax3 = plt.subplots()
                wedges, texts = ax3.pie(sector_series1)
                ax3.pie(sector_series1,autopct='%1.1f%%')
                ax3.legend(wedges,sector_series1.index,title="Sectors",loc="center left",bbox_to_anchor=(1, 0.5))
                plt.title('Top Funded Sectors (By Capital)',fontsize=12)
                st.pyplot(fig3)
            
            if select_option == 'Top Sectors by Startup Count':
                sector_series2= df.groupby('Vertical')['StartUp'].count().sort_values(ascending = False).head()
                fig4,ax4 = plt.subplots()
                ax4.pie(sector_series2,autopct='%1.1f%%')
                wedges,texts = ax4.pie(sector_series2)
                ax4.legend(wedges,sector_series2.index,title="Sectors",loc="center left",bbox_to_anchor=(1, 0.5))
                plt.title('Most Active Sectors (By Number of Deals)',fontsize = 12)

                st.pyplot(fig4)

        st.subheader('Funding Stage Analysis')
        funding_series = df.groupby('Round').agg({'Amount' : 'sum','StartUp' : 'count'}).reset_index().sort_values(by= 'Amount',ascending=False)
        select_option1= st.selectbox('Select Option',['Total Investment by Funding Stage','Number of Deals by Funding Stage'])

        if select_option1 == 'Total Investment by Funding Stage':
            fig5, ax5 = plt.subplots(figsize = (10,4))
            
            ax5.bar(funding_series['Round'],funding_series['Amount'], width= 0.5, label='Amount')
            ax5.set_xticks(funding_series['Round'])
            ax5.set_xticklabels(funding_series['Round'], rotation=45)
            ax5.set_xlabel('Funding Stage')
            ax5.set_yscale('log')  # adjust as per my data
            ax5.get_yaxis().set_major_formatter(plt.ScalarFormatter())
            ax5.set_ylabel('Investment Amount in Cr')
            ax5.set_title('Funding Stage (By Capital)')
            st.pyplot(fig5)
        
        if select_option1 == 'Number of Deals by Funding Stage':
            fig6,ax6 = plt.subplots(figsize = (10,4))
            ax6.bar(funding_series['Round'],funding_series['StartUp'], width= 0.5, label = 'No. of Deals')
            ax6.set_xticks(funding_series['Round'])
            ax6.set_xticklabels(funding_series['Round'], rotation=45)
            ax6.set_xlabel('Funding Stage')
            ax6.set_yscale('log')  # adjust as per my data
            ax6.get_yaxis().set_major_formatter(plt.ScalarFormatter())   # Show normal numbers instead of 10^x
            ax6.set_ylabel('No. of Deals')
            ax6.set_title('Funding Stage (By No. of Deals)')
            st.pyplot(fig6)
        
        col7,col8 = st.columns(2)
        with col7:
            # Year-wise Top Startups
            temp = df.groupby(['Year', 'StartUp'])['Amount'].sum().reset_index().sort_values(['Year', 'Amount'], ascending=[True, False]).groupby('Year').head(1).sort_values('Year')
            st.subheader('Highest Funded Startup Each Year')
            fig6, ax6 = plt.subplots(figsize=(13,7))

            ## Convert Year to string (better x-axis control)
            ax6.bar(temp['Year'].astype(str), temp['Amount'], width = 0.5)

            # Add startup names on bars
            for i in range(len(temp)):
                ax6.text(
                    i,   # position fix 
                    temp['Amount'].iloc[i] + temp['Amount'].max()*0.02,
                    temp['StartUp'].iloc[i],
                    ha='center',
                    fontsize=8
                )
            ax6.set_xlabel('Year')
            ax6.set_ylabel('Funding Amount (Cr)')

            st.pyplot(fig6)

        with col8:
            #Top Investors 
            st.subheader('Top investors (by number of deals)')
            df_temp = df.copy()
            df_temp['Investors'] = df['Investors'].str.split(',')
            top_investor = df_temp['Investors'].explode().str.strip().value_counts()
            top_investor = top_investor[top_investor.index != 'Undisclosed'].head(10)

            fig7,ax7 = plt.subplots(figsize = (13,9))
            ax7.barh(top_investor.index,top_investor.values)
            ax7.set_xlabel('No. Of Deals')
            ax7.set_ylabel('Investor')
            plt.gca().invert_yaxis()  # highest at top
            st.pyplot(fig7)
        
        #Month vs Year Funding
        st.subheader('Funding Heatmap by Month and Year')
        heatmap_data = df.pivot_table(
            values='Amount',
            index='Month',
            columns='Year',
            aggfunc='sum'
        )
        heatmap_data = heatmap_data.drop(columns=2020) #Because only one month data is available for year 2020
        heatmap_data = heatmap_data.apply(lambda x : x.fillna(x.mean()))

        import seaborn as sns

        fig8, ax8 = plt.subplots(figsize=(10,4))
        sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='.0f')
        plt.title('Total funding amount (in crores) for each Month-Year combination')
        st.pyplot(fig8)


        
        


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

    #Top Investors
    top_inves = df.groupby('Investors')['StartUp'].count().sort_values(ascending=False).head()
    st.subheader('Top Investor')

  

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
        
    






