# This program will determin the final grade of the user


def get_stop():
    print("Please combine all final grades and enter number her -->")
    stop = int(input())
    return stop


def get_start():
    print("Please enter the number zero") 
    start = int(input()) 
    return start


def get_increment():
    print("Enter your first grade:")
    increment = int(input())
    return increment 


def get_increment2():
    print("Enter your second grade:")
    increment2 = int(input())
    return increment2  


def while_loop(start, stop, increment, increment2):
    print("While loop counting from " + str(start) + " to " + 
        str(stop) + " by " + str(increment) + " and " + str(increment2) + ":")
    count = start
    while count <= stop:
        print(count)
        count += increment
        count += increment2


def main():
    stop = get_stop()
    start = get_start()
    increment = get_increment()
    increment2 = get_increment2()
    while_loop(start, stop, increment, increment2)


main()  
