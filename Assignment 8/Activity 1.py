# This prgram will return differnt multiples of the users input/parameters


def getValue(name):
    print("Enter " + name + " value: ")
    value = int(input())

    return value


def doLoop(start, stop, increment):
    print("Do loop counting from " + str(start) + " to " + str(stop) + " by " + str(increment) + ".")
    count = start
    while True:    #This simulates a Do Loop
        print(count)
        count = count * increment
        if not(count <= stop): break   #Exit loop


# Main
def main():
    start = getValue("starting")
    stop = getValue("ending")
    increment = getValue("increment")
    doLoop(start, stop, increment)


main()
