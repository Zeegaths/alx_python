"""This script return a different variable for each request"""
import requests
import sys

r = requests.get("https://alu-intranet.hbtn.io/status")
r.headers.get('X-Request-Id')
