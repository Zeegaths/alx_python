"""This sript return a different varaible for every request"""
import requests
import sys

r = requests.get("https://intranet.hbtn.io")
response = r.json()
for title in response['X-Request-Id']:
    print(title['title'])