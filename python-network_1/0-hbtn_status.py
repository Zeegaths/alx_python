"""pulling requests from URL
"""
import requests
response = requests.get("https://alu-intranet.hbtn.io/status")

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")
