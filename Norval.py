import requests

norval = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
content= norval.text
with open ('F:\PythonProject\Spider\《三国演义》.txt','a+') as n:
    n.write(content)

