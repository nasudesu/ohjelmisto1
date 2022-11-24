import requests

key = "8c87a65e1593be9464502d0a55e73f06"
location = input("Give city name: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"
answer = requests.get(request).json()

try:
    answer = requests.get(request)
    if answer.status_code == 200:
        json_answer = answer.json()
        print(f'''Temperature C: {json_answer["main"]["temp"]},'''
              f''' description: {json_answer["weather"][0]["description"]}''')
    elif not answer:
        print("Search returned no results.")

except requests.exceptions.RequestException as e:
    print("Broken")
