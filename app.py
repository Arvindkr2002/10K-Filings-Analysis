import streamlit as st
import pandas as pd
from streamlit_modal import Modal
import plotly.graph_objects as go

# Function to create interactive plot using Plotly
def plot_sentiment_over_years(df, ticker):
    height = 350
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Year'], y=df['Value']))
    
    # Update the layout to center the title
    fig.update_layout(
        title={
            'text': f'Sentiment Over Years ({ticker})',
            'y':0.9,  # Adjust the vertical position of the title
            'x':0.5,  # Center align the title horizontally
            'xanchor': 'center',
            'yanchor': 'top',
        },
        xaxis_title='Year',
        yaxis_title='Sentiment Value',
        height=height
    )
    
    return fig
 
    st.pyplot()
col1, col2, col3 = st.columns([2, 3, 1]) # to centre align the title
with col2:
  st.title('10K-Insights')
  
st.set_option('deprecation.showPyplotGlobalUse', False)

#import text files
with open('/content/AAPL_negatives.txt','r') as fi:
    AAPL_negatives = fi.read()
with open('/content/AAPL_positives.txt','r') as fi:
    AAPL_positives = fi.read()
with open('/content/MSFT_negatives.txt','r') as fi:
    MSFT_negatives = fi.read()
with open('/content/MSFT_positives.txt','r') as fi:
    MSFT_positives = fi.read()

#import CSV files
df_AAPL = pd.read_csv('/content/AAPL_yrly_sentiment.csv')
df_MSFT = pd.read_csv('/content/MSFT_yrly_sentiment.csv')

#create select box
option = st.selectbox("Choose Ticker", ["Choose one", "AAPL", "MSFT"])

if option == 'MSFT':
    #create pop up windows
    negatives = Modal(
        "Negatives", 
        key="Negatives",
    )

    positives = Modal(
        "Positives", 
        key="Positives",
    )
    plot = Modal("plot", key='plot')

    col1, col2, col3 = st.columns([4, 4, 3]) #Align buttons

    #Negative button
    with col2:
        open_negatives = st.button("Negatives")
        if open_negatives: #If button is clicked
            negatives.open() #open the pop-up window

        if negatives.is_open(): #Display content when pop-up window is open
            with negatives.container():
                st.markdown(
                    f"""
                    <div style="overflow-y: scroll; max-height: 300px;">
                    {MSFT_negatives}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    #Positive button
    with col1:
        open_positives = st.button("Positives")
        if open_positives:
            positives.open()

        if positives.is_open():
            with positives.container():
                st.markdown(
                    f"""
                    <div style="overflow-y: scroll; max-height: 300px;">
                    {MSFT_positives}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    #Sentiment Plot button
    with col3:
        open_plot = st.button("Sentiment Over Years")
        if open_plot:
            plot.open()

        if plot.is_open():
            with plot.container():
                st.plotly_chart(plot_sentiment_over_years(df_MSFT, 'MSFT'))

if option == 'AAPL':
    negatives = Modal(
        "Negatives", 
        key="Negatives",
    )

    positives = Modal(
        "Positives", 
        key="Positives",
    )
    plot = Modal("plot", key='plot')

    col1, col2, col3 = st.columns([4, 4, 3])

    with col2:
        open_negatives = st.button("Negatives")
        if open_negatives:
            negatives.open()

        if negatives.is_open():
            with negatives.container():
                st.markdown(
                    f"""
                    <div style="overflow-y: scroll; max-height: 300px;">
                    {AAPL_negatives}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    with col1:
        open_positives = st.button("Positives")
        if open_positives:
            positives.open()

        if positives.is_open():
            with positives.container():
                st.markdown(
                    f"""
                    <div style="overflow-y: scroll; max-height: 300px;">
                    {AAPL_positives}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    
    with col3:
        open_plot = st.button("Sentiment Over Years")
        if open_plot:
            plot.open()

        if plot.is_open():
            with plot.container():
                st.plotly_chart(plot_sentiment_over_years(df_AAPL, 'AAPL'))
