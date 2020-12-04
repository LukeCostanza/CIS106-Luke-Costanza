#This program is determining the avergae grade for the user.


def read_file(scores):
    score_arr = []
    first = 'y'
    file = open(scores, "r")
    for line in file:
        line = line.strip()
        if first == 'y':
            first = 'n'
        else:
            scores = get_score(line)
            try:
                scores = int(scores)
                score_arr.append(scores)
            except ValueError:
                pass
    file.close()
    return score_arr


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
    print("High score: " +str(arr[high_ind]))


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
    print("Low score: " +str(arr[low_ind]))


def print_scores(arr):
    size = len(arr)
    for index in range(0, size):
        print(arr[index])


def main():
    scores = "scores.txt"
    score_arr = read_file(scores)
    print_scores(score_arr)
    get_high(score_arr)
    get_average(score_arr)
    get_low(score_arr)


main()
