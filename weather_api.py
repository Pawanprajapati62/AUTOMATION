import requests

API_KEY ="949316052afd832ec6c06fee192d7d3e"
BASE_URL ="http://api.openweathermap.org/data/2.5/weather"

city = input("city name? :") 
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200: #http staatus code
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 272.15,2)

    print("weather:", weather)
    print("temperature:", temperature)
else:
    print("an error occures!")

    