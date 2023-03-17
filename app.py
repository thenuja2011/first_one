from requests.api import get
from libraries import *
import streamlit as st
import pandas as pd



countries = ['China','India','Sri Lanka','United States','Japan']
data_types = ['cases','deaths','recoveries']
country_code = {'Sri Lanka':'lk','India':'in','China':'CN','Japan':'jp','United States':'us'}

country = st.sidebar.selectbox('What is your country',countries)
days = st.sidebar.slider('days',min_value=1,max_value=90,step=1)
data_type = st.sidebar.multiselect('pick data types',data_types)

total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_recoveries = get_historic_recoveries(country,str(days))


total_df = pd.concat([total_cases,total_deaths,total_recoveries],axis=1).astype(int)




daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_recoveries = get_daily_recoveries(country,str(days))



daily_df = pd.concat([daily_cases,daily_deaths,daily_recoveries],axis=1).astype(int)




yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)

st.title('Covid-19 Visualization Dashboard')





st.metric('Selected Country',country)

#st.image(f"https://flagpedia.net/80x60/{country_code[country]}.png")
 
st.image(f"https://countryflagsapi.com/png/{country_code[country]}")


col1,col2,col3 = st.columns(3)
col1.metric('Yesterday Cases', yesterday_cases)
col2.metric('Yesterday deaths', yesterday_deaths)
col3.metric('Yesterday recoveries', yesterday_recoveries)
st.bar_chart(daily_df)
st.video("https://www.youtube.com/watch?v=CBYyVW66hD8")