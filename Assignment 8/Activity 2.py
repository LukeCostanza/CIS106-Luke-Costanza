# This program is determining the avergae grade for the user. 


def get_value():
    print("How many scores would you like to enter?")
    value = int(input())
    return value


count = 1
sum = 0


def while_loop(count, value, score, sum):
    while count <= value:
      print("Enter score")
      score = int(input())
      sum = sum + score
      count = count + 1

      
def process_average(sum, value):      
    average = sum / value
    print("Your average grade is: " + str(average))


def main():
    value = get_value()
    score = int(input())
    while_loop(count, value, score, sum)
    average = process_average(sum, value)
 
main()
