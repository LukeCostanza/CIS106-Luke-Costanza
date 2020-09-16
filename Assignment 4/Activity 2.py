#this program will determan the users age in months days hours and seconds
age = int(input("How old are you? "))

month = age*12

day = month*365

hour = day*24

seconds = hour*60

print ("your age in months is: " + str(month))

print ("your age in days is: " + str(day))
print ("your age in hours is: " + str(hour))
print ("your age in seconds is: " + str(seconds))
