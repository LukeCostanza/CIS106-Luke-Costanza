# this program will determin the multiples of a given ValueError


def get_value():
    print("enter a value to be multiplied")
    value = int(input())
    return value


def get_expression():
    print("Enter an expression")
    expression = int(input())
    return expression
  


count = 1


def while_loop(value, count, expression, total): 
    while count <= expression: 
      total = value * count
      print(value, '*',count, '=' ,total)
      count = count + 1


def main():
    value = get_value()
    expression = get_expression()
    count = 1
    total = value * count
    while_loop(value, count, expression, total)
    count = count + 1


main()  
