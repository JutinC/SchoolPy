
#importing the Weather class into the main file
#other external libraries
from weather import Weather
from datetime import datetime
import calendar
import random


def tempCheck(weatherList):

    for i in range(6):

        if(int(weatherList[i].lowTemp) < 32):
            print(f"{weatherList[i].day} is a very chilly day.")

        elif(int(weatherList[i].lowTemp) > 60):
            print(f"{weatherList[i].day} is a very hot day.")

        else:
            print(f"{weatherList[i].day} is a warm day.")
        
#Function that uses todays weather to find out the remaining weeks 
#Parameters of todays day and the statistics on today
def weekFill(todayDay, today):

    dayOfWeek = []
    

    dayOfWeek.append(today)

    dayOfWeek[0].displayWeather()
    

    for i in range(6):

        day = (todayDay.weekday() + i + 2) % 7 - 1

        nextDateTime = calendar.day_name[day]

        lowTemp = int(today.lowTemp) + random.randint(-5, 5)

        highTemp = int(today.highTemp) + random.randint(-5, 5)

        averageTemp = int(today.averageTemp) + random.randint(-3, 3)


        if((today.weatherType == "sunny") and (i > 2)):
            weatherType = "cloudy"

        elif((today.weatherType == "cloudy") and (i > 2)):
            weatherType = "stormy"

        elif((today.weatherType == "stormy") and (i > 2)):
            weatherType = "sunny"

        else:
            weatherType = today.weatherType
        

        dayOfWeek.append(Weather(nextDateTime, lowTemp, highTemp, averageTemp, weatherType))

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