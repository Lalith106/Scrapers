from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

def get_currency(in_curr,out_curr):
    url =f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    content = requests.get(url).text
    soup = bs(content,'html.parser')
    rate = soup.find("span",class_="ccOutputRslt").getText()
    return float(rate[0:-4])

print(get_currency('INR',"INR"))
#home page for documentation
@app.route("/")
def home():
    return "<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>"

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate = get_currency(in_cur,out_cur)
    result_dict ={'input_currency':in_cur,'output_currency':out_cur,'rate':rate}
    return jsonify(result_dict)


app.run()