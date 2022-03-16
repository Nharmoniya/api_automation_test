import requests

url="http://123.56.170.43:8888/login"
res=requests.get(url)
print(res.text)