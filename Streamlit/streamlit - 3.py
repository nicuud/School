
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
""")

st.write("""
## Closing price
""")

st.write("""
### Volume
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
ticker0f = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.line_chart(ticker0f.Close)
st.line_chart(ticker0f.Volume)
