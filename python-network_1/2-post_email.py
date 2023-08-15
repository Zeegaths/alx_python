import requests
import sys

def main():
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:           
            print(response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
