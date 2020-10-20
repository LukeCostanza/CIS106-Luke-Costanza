# this program will determin the multiples of a given ValueError


def get_value():# add do loop to make sure value is positive.
    print("enter a value to be multiplied")
    value = int(input())
    while True:
      return value
      if not (value < 0):
        print("Enter a valid value > 0")
        break
    


def get_expression():
    print("Enter an expression")
    expression = int(input())
    while True:
      return expression
      if not (expression < 0):
        print("Enter a valid expression > 0")
        break 
    return expression


def display_expression(value, count, total):
    print(value, '*', count, '=', total)


def display_expressions(value, expression):
    count = 1
    while count <= expression:
        total = value * count
        display_expression(value, count, total)
        count = count + 1


def main():
    value = get_value()
    expression = get_expression()
    display_expressions(value, expression)


main()
