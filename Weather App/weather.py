def show_weather(x):
 # importing requests and json
 import requests, json
 x=str(x)
 # base URL
 BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
 fw = open(r'Weather App\weather.txt')
 API_KEY=fw.read()
 URL = BASE_URL + "q=" + x + "&appid=" + API_KEY
 st=""
 # HTTP request
 response = requests.get(URL)
 # checking the status code of the request
 if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = (int(main['temp'])-273.0)
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # weather report
    report = data['weather']
    st+=f"{x:-^30}"+'\n'+f"Temperature: {temperature} Celsius"+'\n'+f"Humidity: {humidity} g/kg"+'\n'+f"Pressure: {pressure} Pa"+'\n'+f"Weather Report: {report[0]['description']}"
    return(st)
 else:
    # showing the error message
    return("Provide Valid Input")
