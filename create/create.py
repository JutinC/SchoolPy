
#importing the Weather class into the main file
#other external libraries
from weather import Weather
from datetime import datetime
import calendar
import random

#procedure to pick out the specific temperatures in a week
def tempCheck(weatherList):
    #makes a loop for the remaining 6 days to test if it will be cold or hot
    for i in range(6):
        #If its under 32 degrees its cold
        if(int(weatherList[i].lowTemp) < 32):
            print(f"{weatherList[i].day} is a very chilly day.")
        #If its above 60 degrees its hot
        elif(int(weatherList[i].lowTemp) > 60):
            print(f"{weatherList[i].day} is a very hot day.")
        #otherwise it is just warm
        else:
            print(f"{weatherList[i].day} is a warm day.")
        
#Function that uses todays weather to find out the remaining weeks 
#Parameters of todays day and the statistics on today
def weekFill(todayDay, today):
    #Creates the list
    dayOfWeek = []
    
    #appends the first day to the list
    dayOfWeek.append(today)
    #displays the weather today
    dayOfWeek[0].displayWeather()
    
    #loops the next 7 days for the week predictions
    for i in range(6):
        #finds the next day in the list as an integer
        day = (todayDay.weekday() + i + 2) % 7 - 1
        #sets it as an actual day of the week
        nextDateTime = calendar.day_name[day]
        #randomizes the low temperature for the day
        lowTemp = int(today.lowTemp) + random.randint(-5, 5)
        #randomizes the high temperature for the day
        highTemp = int(today.highTemp) + random.randint(-5, 5)
        #randomizes the average temperature for the day
        averageTemp = int(today.averageTemp) + random.randint(-3, 3)
        #Changes the weather after 3 days
        #if its sunny it turns cloudy
        if((today.weatherType == "sunny") and (i > 2)):
            weatherType = "cloudy"
        #if its cloud turns stormy
        elif((today.weatherType == "cloudy") and (i > 2)):
            weatherType = "stormy"
        #if stormy turns sunny
        elif((today.weatherType == "stormy") and (i > 2)):
            weatherType = "sunny"
        #otherwise it will remain the same
        else:
            weatherType = today.weatherType
        
        #Appends the next day into the list
        dayOfWeek.append(Weather(nextDateTime, lowTemp, highTemp, averageTemp, weatherType))
        #displays the day on the list +1 because first day is already used
        dayOfWeek[i + 1].displayWeather()
        
    return dayOfWeek

#defining main
def main():
    
    #Gets todays date
    todayDateTime = datetime.now()
    #Prints todays day
    print("Todays is {}".format(calendar.day_name[todayDateTime.weekday()]))
    #Asks for user input
    userLowTemp = input("What's the low temperature\n")
    userHighTemp = input("Whats the high temperature?\n")
    userAvgTemp = input("Whats the average temperature??\n")
    userWeatherType = input("Whats the weather?\n")
    

    #Creates an object to open up the weather class
    today = Weather(calendar.day_name[todayDateTime.weekday()], userLowTemp, userHighTemp, userAvgTemp, userWeatherType)
    #Gets the list of the week 
    weatherList = weekFill(todayDateTime, today)
    #calls the procedure to print out which days are cold, hot, and warm
    tempCheck(weatherList)

#calling main
if(__name__=="__main__"):
    main()