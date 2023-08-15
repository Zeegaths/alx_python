"""This script return a different variable for each request"""
import requests
import sys

def main():
    "receive and process the URL"
    url = "https://alu-intranet.hbtn.io/status"  # Get the URL from user input

    try:
        response = requests.get(url)
        if response.status_code == 200:
            headers = response.headers
            x_request_id = headers.get('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id header not found in the response headers.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
