#This program displays the users input in a different order the it is recieved.


def get_name():
    while True:
        print("Enter name (First Last):")
        name = input()
        error_1 = get_error_1(name)
        if error_1 == "n":
            error_2 = get_error_2(name)
            if error_2 == "n":
                return name


def get_error_1(name):
    index = name.find(" ")
    check = name[index + 1:]
    index = check.find(" ")
    if index >= 0:
        print("Too many spaces!")
        error_1 = "y"
    else:
        error_1 = "n"
    return error_1


def get_error_2(name):
    last = get_last(name)
    if last == "error":
        print("No last name!")
        error_2 = "y"
    else:
        error_2 = "n"
    return error_2


def get_last(name):
    index = name.find(" ")
    if index > 0:
        last = name[index + 1:]
    else:
        last = "error"
    return last


def get_first(name):
    index = name.find(" ")
    first = name[0: index]
    return first


def display_name(first, last):
    print(last + ", " + first[0] + ".")


def main():
    name = get_name()
    last = get_last(name)
    first = get_first(name)
    display_name(first, last)

main()
