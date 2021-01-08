print("Hello world")
# maths
print(10**2)
print(9/3)
print(5 * 7)
print(5 + 5)
print(20 - 10)
import math
print(math.sin(3))
print(math.pi)
print(math.sin(math.pi))
print(math.sin(math.sqrt(4)))
# variables
temp_celsius = 10.0
print( "Temperature in Fahreinheit is", temp_celsius * 9/5 + 32)
# updating variables
name = "Brian otieno"
cars = 1
temp_celsius = 15.0
temp_fahreinheit = 9/5 * temp_celsius + 32
print("Temperature in celsius is now", temp_celsius)
print("Temperature in celsius is", temp_celsius," and temperature in fahreinheit is", temp_fahreinheit)
# data type
print(type(name))
print(type(temp_celsius))
print(type(cars))
# character input
surname = input("What is your name")
age = input("how old are you")
print(surname +' is a nice name and from your age of', age ,"you are  still young!")
station_name = "CK1"
station_lat = 258506.417
station_lon =9855083.229
station_id = 1
station_type = "control"
# converting to another data type
station_id_str = str(station_id)
print(type(station_id_str))
print("Station name is", station_name + ": ," +station_id_str)
# creating a list
station_names = ['CK1','TMH01', 'TR2', 'TR3', 'TR4', 'TR5', 'TMHO2', 'TMHO3']
print(station_names)
print(len(station_names))
print(station_names[1])
print(station_names[-8])
# modifying list value
station_names[0] ="CK2"
print(station_names)
print(type(station_names))
# removing a station to list
del station_names[0]
print(station_names)
# adding a station
station_names.append("TMH04")
print(station_names)
# counting no of stations appears
print(station_names.count('TMH04'))
# reverse list of stations
station_names.reverse()
print(station_names)
#sorting alphabetically
station_names.sort()
print(station_names)




