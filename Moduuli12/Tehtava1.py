import requests

request = "https://api.chucknorris.io/jokes/random"
answer = requests.get(request).json()


try:
    answer = requests.get(request)
    if answer.status_code==200:
        json_answer = answer.json()
        print(json_answer["value"])
except requests.exceptions.RequestException as e:
    print("Invalid request.")