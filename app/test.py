import requests
        
url = "https://fastah-ip.p.rapidapi.com/whereis/v1/json/auto"

headers = {
            "X-RapidAPI-Host": "fastah-ip.p.rapidapi.com",
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
        }

response = requests.request("GET", url, headers=headers)
if response.status_code == 200:
    location = response.locationData.cityName
    temp = location.split(',')
    state = temp[1]
    state = state[1:]
    url = "/v2/states/"+state+".json"
    response2 = requests.request("GET", url)
    if response2.status_code == 200:
        data = response.json()
        confidence = 1
        statement = "This is the data"
    else:
        confidence = 0
        statement = "Sorry I could not find this data."
elif response.status_code == 404:
    statement = "404 Error"
else:
    statement = "400 Error"

print(statement)

        
