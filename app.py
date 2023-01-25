import yfinance as yf
import streamlit as st
import pandas as pd


st.write(
    '''
# Простое веб-приложение для просмотра котировок акций компании Apple 

Ниже приведены **максимальная** и **минимальная** цена акций каждого 
торгового дня и **объем торгов**
''')
tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2018-1-1', end='2021-1-1')

tickerDf.rename(columns={'High':'Макс.', 'Low':'Мин.', 'Volume':'Объем торгов'}, inplace=True)
st.write('### Минимальная и максимальная цена акций')
st.line_chart(y=('Макс.', 'Мин.'), data=tickerDf)

st.write('### Количество торговых операций')
st.line_chart(tickerDf['Объем торгов'])
tickerDf.index = pd.to_datetime(tickerDf.index)
