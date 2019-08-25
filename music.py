import requests

m=requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
b=m._content
with open ('rainbow.mp3','wb') as rb:
    rb.write(b)