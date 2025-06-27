import requests
url = "https://graph.facebook.com/v23.0/me?fields=posts%7Blink%7D&access_token=EAAsd9RTQz7ABO18oX3qZBNfJGPiQlweB1UZC6nvXMGl8S6824Sv1v33okpmnRxC1UmjFymoQFnaRPDCzS36TYgNYU91bT5k0qQHEQOB7zAxfdNyRghQi2pnarszBfHYrFujIMZAdqquIsMbGgV8yLZAhZBG04VyruhimLDnqc3rAEJBmItfZCS7fekNMGEsOGfxxOeE5tZAzTQlauw7ik61pZAVFdv25eWtJ4HV8"

cont = requests.get(url)
response =cont.json()
#print(response)
img1=response['posts']['data'][10]['id']
print(img1)
image_bytes = requests.get(img1)
#print(image_bytes)
print(image_bytes.headers.get('Content-Type'))
url = f"https://graph.facebook.com/v23.0/{g1}?fields=full_picture&access_token=EAAsd9RTQz7ABO18oX3qZBNfJGPiQlweB1UZC6nvXMGl8S6824Sv1v33okpmnRxC1UmjFymoQFnaRPDCzS36TYgNYU91bT5k0qQHEQOB7zAxfdNyRghQi2pnarszBfHYrFujIMZAdqquIsMbGgV8yLZAhZBG04VyruhimLDnqc3rAEJBmItfZCS7fekNMGEsOGfxxOeE5tZAzTQlauw7ik61pZAVFdv25eWtJ4HV8"
img1=requests.get(url).content
with open("image.jpg",'wb')as file:
    file.write(img1)