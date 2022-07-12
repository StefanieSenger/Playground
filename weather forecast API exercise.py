# weather forecast API exercise

import os; os.system("pip install requests")
import requests
response = requests.get("https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()
# Do not modify the code above

def weather_forecast(response):
    for index, key in enumerate(response):
        if key == 'city':
            for ele in response[key]:
                if ele == 'name':
                    city = response[key][ele]
    for index, key in enumerate(response):
        #print(index, key, response[key])
        if index == 3:
            #print(response[key])
            for ele in response[key]:
                #print(ele) #, response[key][ele])
                for item in ele:
                    #print(item, ele[item])
                    #if item == 'dt_txt':
                        #if '2022-07-08' in ele[item]:
                            #pass
                            #print('date for tomorrow')
                    if item == 'weather':
                        for part in ele[item]:
                            for tinithing in part:
                                if tinithing == 'main':
                                    forecast = part[tinithing]
    return f'The weather in {city} tomorrow is {forecast}'

print(weather_forecast(response))
