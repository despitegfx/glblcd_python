import pyowm

while True:
    print ("................................")
    PlaceName=str(input("Name of place: "))
    print ("")

    owm = pyowm.OWM ('bf45390a352169d3a24e4ea5363c3c49')
    observation = owm.weather_at_place(PlaceName)
    w = observation.get_weather()
 
    #print (w.get_wind())
    #print (w.get_humidity())
    #print (w.get_temperature())
    #print (w.get_pressure())
    print (w.get_wind())
