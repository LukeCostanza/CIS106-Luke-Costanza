#This program is determining the avergae grade for the user.


def get_grades():
    array = []
    score = 0
    while score >= 0:
        print("Enter a score value greater then zero:")
        score = int(input())
        if score >= 0:   
            array.append(score)
        else:
            return array


def get_high(arr):
    size = len(arr)
    high = arr[0]
    for index in range(1, size):
        if arr[index] > high:
            high = arr[index]
    print("High score: " +str(high))


def get_average(arr):
    size = len(arr)
    sum = 0
    for index in range(0, size):
        sum = sum + arr[index]
    average = sum / size
    print("Average score: " +str(average))


def get_low(arr):
    size = len(arr)
    low = arr[0]
    for index in range(1, size):
        if arr[index] < low:
            low = arr[index]
    print("Low score: " +str(low))


def print_sort(arr):
    arr.sort() 
    print("Here are your scores from low to high!")
    print(arr)
   

def main():
    array = get_grades()
    get_high(array)
    get_average(array)
    get_low(array)
    print_sort(array)


main()
