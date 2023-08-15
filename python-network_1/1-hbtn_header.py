"""This script return a different variable for each request"""
import requests
import sys

r = requests.get("https://intranet.hbtn.io")
x_request_id = r.headers.get('X-Request-Id')
print("{x_request_id}")