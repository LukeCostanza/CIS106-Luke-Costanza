def processAge(age):
    print("What is your dogs age?: ")

def variableage(age):
    age = age * 7

def variablename(name):
    print("What is your dogs name?: ")

# Main
# This program displays the age of a dog in dog years
# In relation to human years
print("Type your dogs name")
name = input()
print("Type your dogs age in human years:")
age = int(input())
age = age * 7
print("Your dogs age in dog years is: " + str(age))
