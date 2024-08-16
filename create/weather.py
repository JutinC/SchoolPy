#Weather class
class Weather():
    #Initates the fields of the weather class
    def __init__(self, day, lowTemp, highTemp, averageTemp, weatherType):
        self.day = day
        self.lowTemp = lowTemp
        self.highTemp = highTemp
        self.averageTemp = averageTemp
        self.weatherType = weatherType
    
    #getters and setters
    #Accesses the day variable in the class
    def getDay(self):
        return self.day
    
    #Mutates the day variable to be the day set originally
    def setDay(self, day):
        self.day = day
    #get user validation
    def getLowTemp(self):
        return self.lowTemp
    #sets the value of low Temp
    def setLowTemp(self, lowTemp):
        self.lowTemp = lowTemp
    #gets the high temperature    
    def getHighTemp(self):
        return self.highTemp
    #sets it equal to the private value
    def setHighTemp(self, highTemp):
        self.highTemp = highTemp
    #gets the average temperature
    def getAverageTemp(self):
        return self.averageTemp
    #sets it as the value
    def setAverageTemp(self, averageTemp):
        self.averageTemp = averageTemp
    #finds the weather type
    def getWeatherType(self):
        return self.weatherType
    #sets the weather type
    def setWeatherType(self, weatherType):
        self.weatherType = weatherType
        
    #Displays the weather
    def displayWeather(self):
        print("Weather Report")
        print(f"On {self.getDay()}, the low temperature is {self.getLowTemp()} degrees, the high temperature is {self.getHighTemp()} degrees, the average temperature is {self.getAverageTemp()} degrees, and it is {self.getWeatherType()} outside.\n")