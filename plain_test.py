import requests

url = "http://127.0.0.1:8000/predict"

payload = {
    "cloud": 60,
    "humidity": 78,
    "windspeed": 12,
    "dewpoint": 24,
    "day": 15,
    "pressure": 1013.5,
    "maxtemp": 32,
    "mintemp": 25,
    "temparature": 28.5,
    "sunshine": 6.5
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)