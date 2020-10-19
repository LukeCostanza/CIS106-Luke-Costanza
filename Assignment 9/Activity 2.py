# This program is determining the avergae grade for the user.


print("When you are finished entering all grades please enter a negative value using '-' symbol.")


def while_loop():
    count = 0
    sum = 0
    while True:
        print("Enter grade:")
        score = int(input())
        if score < 0:
            break
        sum = sum + score
        count = count + 1
    process_average(sum, count)
    return sum


def process_average(sum, count):
    average = sum / count
    print("Your average grade is: " + str(average))


def main():
    while_loop()


main()
