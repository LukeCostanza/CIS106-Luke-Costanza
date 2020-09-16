#This program will determin the cost and amount of paint needed for a room (6)

length = int(input("length of room in Ft: "))
width = int(input("width of room in Ft: "))
height = int(input("height of room in Ft: "))

TotalArea = (2 * length * height + 2 * width * height)

price = float(input("price for a gallon of paint to the .00 decimal point (Ex: 10.24) "))
square = int(input("amount of square feet your gallon of paint will cover: "))

gallon = TotalArea / square
RoundedGallon = (.9999 + gallon)
cost = price * RoundedGallon

print(str("size of your room in square Ft is: ") + str (TotalArea)+ str(" Square Ft"))
print(gallon)
print(cost)
