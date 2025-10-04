import requests

x = requests.get("https://w3shcools.com/python/demopage.htm")

print(x.text)