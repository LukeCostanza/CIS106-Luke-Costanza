#This program will print out the users input on seperate lies and with no extra input data.


def get_string():
    print("Enter data seperated by commas.")
    string = input()
    while True:
        index = string.find(",")
        if index > 0:
            data = string[0: index]
            data = data.strip()
            print(data)
            string = string[index + 1:]
            print(string)
        else:
            string = string.strip()
            print(string)
            break


def main():
    get_string()


main()
