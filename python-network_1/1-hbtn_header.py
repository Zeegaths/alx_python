"""This script return a different variable for each request"""
import requests
import sys

# You should specify the URL you're testing against
url = "http://0.0.0.0:5050"  # Update this to the actual URL you want to test

try:
    response = requests.get(url)
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        print(f"X-Request-Id: {x_request_id}")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")
