#This program is determining the avergae grade for the user.


def get_value():
    print("How many grades would you like to enter?")
    value = int(input())
    return value


def build_array(size):
    array = [None] * size
    for index in range(0, size):
        print("Enter grade")
        score = int(input())
        array[index] = score
    return array


def get_high(size, arr):
    high = arr[0]
    for index in range(1, size):
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
    low = arr[0]
    for index in range(1, size):
        if arr[index] < low:
            low = arr[index]
    print("Low score: " +str(low))     
   

def main():
    value = get_value()
    array = build_array(value)
    get_high(value, array)
    get_average(value, array)
    get_low(value, array)


main()
