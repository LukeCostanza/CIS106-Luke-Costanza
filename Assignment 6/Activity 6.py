# This program will determin the cost and amount of paint needed for a room (6)


def display_results(total_area, gallon, cost):
    print(str("size of your room in square Ft is: ") + str(total_area) + str(" Square Ft"))
    print(gallon)
    print(cost)


def get_length():
    print ("length of room in Ft: ")
    length = int(input())
    return length


def get_width():
    print ("width of room in Ft: ")
    width = int(input())
    return width


def get_height():
    print ("height of room in Ft: ")
    height = int(input())
    return height


def process_area(length, height, width):
    Total_area = 2 * length * height + 2 * width * height
    return Total_area


def get_price():
    print ("price for a gallon of paint to the .00 decimal point (Ex: 10.24) ")
    price = int(input())
    return price


def get_square():
    print ("amount of square feet your gallon of paint will cover: ")
    square = int(input())
    return square


def process_gallon(total_area, square):
    gallon = total_area / square
    return gallon


def process_Rgallon(gallon):
    Rounded_gallon = .9999 + gallon
    return Rounded_gallon


def process_cost(price, Rounded_gallon):
    cost = price * Rounded_gallon
    return cost


def main():
    length = get_length()
    width = get_width()
    height = get_height()
    total_area = process_area(length, height, width)
    price = get_price()
    square = get_square()
    gallon = process_gallon(total_area, square)
    Rounded_gallon = process_Rgallon(gallon)
    cost = process_cost(price, Rounded_gallon)
    results = display_results(total_area, gallon, cost)


main()
