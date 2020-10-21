# this program will determin the multiples of a given ValueError
  # cites used: https://hplgit.github.io/primer.html/doc/pub/input/._input-readable007.html

def get_value():
    while True:
      print("enter a value to be multiplied")
      value = int(input())
      if value > 0:
        return value
      if not (value < 0):
        break
      Exception
      print("Enter a valid value > 0")  
        
    
def get_expression():
    while True:
      print("Enter an expression")
      expression = int(input())
      if expression > 0:
        return expression
      if not (expression < 0):
        break 
      Exception
      print("Enter a valid expression > 0")  


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
