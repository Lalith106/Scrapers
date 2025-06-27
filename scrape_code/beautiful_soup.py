from bs4 import BeautifulSoup as bs
import requests

def get_currency(in_curr,out_curr):
    url =f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    content = requests.get(url).text
    #print(content)
    soup = bs(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").getText()
    return float(rate[0:-4])

print(get_currency('INR',"INR"))