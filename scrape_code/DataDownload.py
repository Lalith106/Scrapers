import yfinance as yf
import requests
import time
from datetime import datetime

"""A ticker symbol is a unique set of characters, usually letters, 
assigned to a publicly traded company for identification on stock exchanges 
and trading platforms"""

ticker =input("Enter ticker Symbol: ")
from_date= input('Enter  start Date in %Y-%m-%d format:')
to_date =input("Enter end Date in %Y-%m-%d' format: ")

data = yf.download(ticker,start=from_date,end=to_date)
data.to_csv(f"{ticker}_{from_date}_{to_date}.csv")