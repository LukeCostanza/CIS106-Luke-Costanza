# This program displays the age of a dog in dog years in relation
# to human years


def display_results(name, dog_age):
    print(name + " is " + str(dog_age) + " in dog years.")


def process_age(age):
    if age <= 2:
        dog_age = age * 10.5
    else:
        dog_age = (age - 2) * 4 + 21
    return dog_age


def get_name():
    print("What is your dogs name?: ")
    name = input()
    return name


def get_age():
    print("What is your dogs age?: ")
    age = int(input())
    return age


def main():
    name = get_name()
    age = get_age()
    dog_age = process_age(age)
    display_results(name, dog_age)


main()
