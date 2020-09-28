def displayResults(name, dogAge):
    print(name + " is " + str(dogAge) + " in dog years.")

def processAge(age):
    dogAge = age * 7
    
    return dogAge

def getName():
    print("What is your dogs name?: ")
    name = input()
    
    return name

def getAge():
    print("What is your dogs age?: ")
    age = int(input())
    
    return age

# Main
# This program displays the age of a dog in dog years in relation to human years
name = getName()
age = getAge()
dogAge = processAge(age)
displayResults(name, dogAge)
