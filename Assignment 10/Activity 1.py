# this program will determin the multiples of a given ValueError


def get_value():
    print("enter a value to be multiplied")
    value = int(input())
    return value


def get_expression():
    print("Enter an expression")
    expression = int(input())
    return expression


def display_expression(value, count, total):
    print(value, '*', count, '=', total)


def display_expressions(value, expression):
    for count in range(1, expression + 1, 1):
        total = value * count
        display_expression(value, count, total)


def main():
    value = get_value()
    expression = get_expression()
    display_expressions(value, expression)


main()
