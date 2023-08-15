"""This module sends a POST request with email as parameter"""
import requests
import sys

url = "http://0.0.0.0:5000/post_email"
email = "hr@holbertonschool.com"

r = requests.post(url, params=email)
print(r)