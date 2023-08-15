"""This sript return a different varaible for every request"""
import requests
import sys

r = requests.get("https://intranet.hbtn.io")
print("r.headers{['X-Request-Id']}")
