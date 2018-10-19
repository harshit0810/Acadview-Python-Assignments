#QUESTION-3
class temperature:
    def convertFahrenheit(self,c):
        print("temp in \N{degree sign}F",c*1.8+32)
        
    def convertCelcius(self,f):
        print("temp in \N{degree sign}C",(f-32)*(5/9))
temp=temperature()
temp.convertFahrenheit(int(input("enter the temp. in celcius:- ")))
temp.convertCelcius(int(input("enter the temp. in fahrenheit:- ")))
