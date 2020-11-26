#This program is determining the avergae grade for the user.


def read_file(scores):
    name_arr = []
    score_arr = []
    file = open(scores, "r")
    for line in file:
        line = line.strip()
        name = get_name(line)
        score = get_score(line)
        name_arr.append(name)
        score_arr.append(score)
    high = get_high(score_arr)
    print("High score")
    print(name_arr[high])
    print (str(score_arr[high]))
    average = get_average(score_arr)
    print (str(average))
    low = get_low(score_arr)
    print("Low score")
    print(name_arr[low])
    print (str(score_arr[low]))
    file.close()
    print("")


def get_name(line):
    index = line.find(",")
    name = line[0: index]
    return name


def get_score(line):
    index = line.find(",")
    score = line[index + 1:]
    return score


def get_high(arr):
    size = len(arr)
    high = int(arr[0])
    for index in range(1, size):
        if int(arr[index]) > high:
            high = int(arr[index])
            high_ind = index
    return high_ind


def get_average(arr):
    size = len(arr)
    sum = 0
    for index in range(0, size):
        sum = sum + int(arr[index])
    average = sum / size
    rounded_average = round(average, 2)
    print("Average score: " +str(rounded_average))


def get_low(arr):
    size = len(arr)
    low = int(arr[0])
    for index in range(1, size):
        if int(arr[index]) < low:
            low = int(arr[index])
            low_ind = index
    return low_ind


def main():
    scores = "scores.txt"
    read_file(scores)


main()
