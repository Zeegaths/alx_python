"""pulling requests from URL
"""
import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
response.text
type(response.text)