import requests
url="https://api.languagetool.org/v2/check"
data ={
    'text':'Tis is a nize dayy!',
    'language':'auto'
}
response =requests.post(url,data=data)
print(type(response.text))
result = response.content
print(result)
print(type(result))