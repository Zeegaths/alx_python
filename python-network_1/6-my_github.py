import requests
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data.get("id")
            if user_id is not None:
                print(f"User ID: {user_id}")
            else:
                print("User ID not found in the response.")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
