"""pulling requests from URL
"""
import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
print("type:{}".format(type(response.text)))  
print("content:{}".format(response.text)) 