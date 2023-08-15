"""This script return a different variable for each request"""
import requests
import sys

def main():
    url = sys.argv[1]
    r = requests.get(url)
    r2 = r.headers.get('X-Request-Id')
    print (r2)
    
if __name__ == "__main__":
    main()


