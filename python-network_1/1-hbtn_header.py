"""This script return a different variable for each request"""
import requests
import sys

url = input("Enter a URL")
r = requests.get("url")
r.headers.get('X-Request-Id')
