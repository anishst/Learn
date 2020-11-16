# app2.py
# https://kanoki.org/2020/07/04/create-interactive-dashboard-in-python-using-streamlit/
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def app():
    st.title('APP2')
    st.write('Welcome to app2')
    state_csv_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
    us_total_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'

    df = pd.read_csv(us_total_url, parse_dates=['date'])
    dfstate = pd.read_csv(state_csv_url)

    st.title("Covid19 USA Data from Wikipedia")
    st.markdown(
        """
        This app is for visualizing the Covid19 data for USA which is collected 
        from the wikipedia site https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States.        
        User can select the Metrics Type from the drop-down list to see the trend in last 15 days
        """
    )

    st.markdown("## " + 'TotalCases/Deaths/Recoveries Trend')
    st.markdown("#### " + "What Trends would you like to see?")

    selected_metrics = st.selectbox(
        label="Choose...", options=['TotalCases', 'Deaths']
    )

    # Create traces
    fig = go.Figure()
    if selected_metrics == 'TotalCases':
        fig.add_trace(go.Scatter(x=df.date, y=df.cases,
                                 mode='lines',
                                 name='TotalCases'))
    if selected_metrics == 'Deaths':
        fig.add_trace(go.Scatter(x=df.date, y=df.deaths,
                                 mode='markers', name='Deaths'))

    st.plotly_chart(fig, use_container_width=True)

    st.sidebar.title("State-Wise Data")
    State_list = st.sidebar.selectbox(
        'state',
        dfstate.state)