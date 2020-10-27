# This program is determining the avergae grade for the user.


def get_value():
    print("How many grades would you like to enter?")
    value = int(input())
    return value

def get_score():
    score = 0
    print("Enter grade")
    while score <= 0:
        score = int(input())
        if score > 0:   
            return score
        if (score < 0):
            print("Enter a valid value > 0")  


def while_loop(value):
    count = 1
    sum = 0
    while count <= value:
        score = get_score()
        sum = sum + score
        count = count + 1
    return sum


def process_average(sum, value):
    average = sum / value
    print("Your average grade is: " + str(average))


def main():
    value = get_value()
    sum = while_loop(value)
    process_average(sum, value)


main()
