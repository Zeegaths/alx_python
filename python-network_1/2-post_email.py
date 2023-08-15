"""This module sends a POST request with email as parameter"""
import requests
import sys

def main():
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {"email": email}
    
    try:
        response = requests.post(url, data=payload)  
        if response.status_code == 200:
            response_text = response.text
            print("Response Body:")
            print(response_text)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()





