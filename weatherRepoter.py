def get_weather_report(temperature):
    if temperature < 22 :
        print("Cold")
    elif temperature >= 22 and temperature < 35 :
        print("Warm")
    else:
        print("Hot")
    # Complete this function


temperature = int(input())
# Call the get_weather_report function
get_weather_report(temperature)