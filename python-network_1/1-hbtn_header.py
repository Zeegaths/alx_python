"""import required modules"""
import requests
import sys

# function carrying the main logic of the script
def func_1():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)
    
    # assign the url as the first command line argument
    url = sys.argv[1]
    
    try:
        # send a GET request to the specified URL
        response = requests.get(url)
        # check if the request is successful
        if response.status_code == 200:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id not contained in the response header.")
        else:
            print(f"Request failed: {response.status_code}")
    # catch any exceptions that might arise
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    func_1()
