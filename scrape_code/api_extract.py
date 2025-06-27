import requests

def get_news(country,api_key="bbf54373a64a4c9d8c593cac284ed26d"):
    url =f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r =requests.get(url)
    content = r.json()
    results=[]
    print(content)
    articles = content['articles']
    for art in articles:
        results.append(f"TITLE\n {art['title']}, \nDESCRIPTION\n {art['description']}")
    return (results)

def get_climate_details_by_city(city_ID,city_name,API_KEY="afb2d355d51b58d8b7e5677f16557c6f"):
    url =f"http://api.openweathermap.org/data/2.5/forecast?id={city_ID}&appid={API_KEY}"
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}"
    print(url)
    response = requests.get(url)
    content= response.json()
    list=content['list']
    city =content['city']['name']
    with open("weather_report.txt",'w')as f:
        f.write("City | Time | Temp | Description\n")

        for ele in list:
            time = ele['dt_txt']
            temp=ele['main']['temp']
            descr= ele['weather'][0]['description']
            line =f"{city} | {time} | {temp} | {descr}\n"
            f.write(line)

    print("Weather data saved successfully")

get_climate_details_by_city(1264527,'Chennai')

