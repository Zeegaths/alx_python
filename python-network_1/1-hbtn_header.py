"""This script return a different variable for each request"""
import requests
import sys

r = requests.get("https://intranet.hbtn.io")
r.headers['X-Request-Id']
print("{r.headers}")