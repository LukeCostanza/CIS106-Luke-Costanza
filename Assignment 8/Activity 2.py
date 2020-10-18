# This program is determining the avergae grade for the user. 


def get_value():
    print("How many scores would you like to enter?")
    value = int(input())
    return value


def while_loop(value, sum):
    count = 1
    sum = 0
    while count <= value:
      print("Enter score")
      score = int(input())
      sum = sum + score
      count = count + 1

      
def process_average(value):      
    average = sum / value
    print("Your average grade is: " + str(average))
    return average



def main():
  value = get_value()
  while_loop(value, sum)
  average = process_average(value)
 
main()
