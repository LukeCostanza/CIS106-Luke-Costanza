#This program is determining the avergae grade for the user.


def get_value():
    print("How many grades would you like to enter?")
    value = int(input())
    return value


def build_f(size):
    f = []
    for index in range(0, size):
        print("Enter grade")
        score = int(input())
        f.append(score)
    return f


def get_high(size, arr):
    high = 0
    for index in range(0, size):
        if arr[index] > high:
            high = arr[index]
    print("High score: " +str(high))


def get_average(size, arr):
    sum = 0
    for index in range(0, size):
        sum = sum + arr[index]
    average = sum / size
    print("Average score: " +str(average))



def get_low(size, arr):
    low = 999
    for index in range(0, size):
        if arr[index] < low:
            low = arr[index]
    print("Low score: " +str(low))     
   

def main():
    value = get_value()
    f = build_f(value)
    get_high(value, f)
    get_average(value, f)
    get_low(value, f)


main()
