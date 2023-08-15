"""pulling requests from URL
"""
import requests
url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)
"""Modifying the output"""
if response.status_code == 200:
    """Modifying the output"""
    data = response.json()
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    print(
        f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")
