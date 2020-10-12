# This program uses a loop to generate a list of multiplication expressions for a given value


def get_value(name):
    print("Enter " + name + " value:")
    value = int(input())
    return value


def while_loop(number, expressions, multiple):
    print (str("While looping your number " + str(number) + " will be multiplied by " + str(multiple) + " , " + str(expressions) + " times!"))
    count = number
    while count <= expressions:
        print(count)
        count = count * multiple


def main():
    number = get_value("number")
    expressions = get_value("expressions")
    multiple = get_value("multiple")
    while_loop(number, expressions, multiple)


main()
