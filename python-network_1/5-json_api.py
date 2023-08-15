import requests
import sys

def main():
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        try:
            json_data = response.json()

            if json_data:
                user_id = json_data.get("id")
                user_name = json_data.get("name")

                if user_id is not None and user_name is not None:
                    print(f"[{user_id}] {user_name}")
                else:
                    print("Not a valid JSON")

            else:
                print("No result")

        except ValueError:
            print("Not a valid JSON")
            
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
