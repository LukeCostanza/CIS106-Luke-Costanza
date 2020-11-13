#This program is determining the avergae grade for the user.


def get_grades():
    array = []
    size = 0
    score = 0
    while score >= 0:
        print("Enter a score value greater then zero:")
        score = int(input())
        if score >= 0:   
            array.append(score)
            size = size + 1
    print(size)
    get_high(size, array)
    get_average(size, array)
    get_low(size, array)



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
    get_grades()

main()
