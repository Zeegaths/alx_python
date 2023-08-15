"""pulling requests from URL
"""
import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
