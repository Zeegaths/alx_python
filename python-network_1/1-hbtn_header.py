"""This sript return a different varaible for"""
import requests
import sys

r = requests.get("https://intranet.hbtn.io")
response = r.headers['X-Request-Id']
print(response)