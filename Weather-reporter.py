
city = input("enter the city name: ")

temp = float(input("enter the temp in Celsius: "))

print("city", city , "temperature in C", temp)

if temp > 40000:
    print("HOW TH ARE YOU SURVIVING UR LIVIN ON THE SUN?")
elif temp > 30:
    print("yo you better be drinking water son")
elif temp > 25:
    print("Still hot ")
elif temp > 20:
    print("twin this is the CLOSE TO PERFECT weather")
elif temp > 15:
    print("twin this is the PERFECT weather to camp")
elif temp > 10:
    print("good weather not that bad tbh")
elif temp > 5:
    print("tbh this is a bit cold but not that bad js get a thin jacket")
elif temp > 0:
    print("dead point get ready for the scandavian winter")
elif temp > -5:
    print("get a medium jacket")
elif temp > -10:
    print("snow has already formed a bit get snow gear")
elif temp > -15:
    print("peak winter get a thick jacket and snow gear also have a snow ball fight")
else:
    print("twin this is the coldest weather possible get a thick jacket and snow gear and stay inside unless its minus 20 or stmg")

import datetime
import calendar

now = datetime.datetime.now()
print("city", city)

print("time now: ", now)

print(calendar.calendar(now.year))