
import sys
import requests

def main():
    url = sys.argv[1]
    r = requests.get(url)

    r1 = r.status_code

    if r1 >= 400:
        print("Error code: {}".format(r1))
    elif r1 < 400:
        print("Regular request")

if __name__ == "__main__":
    main()