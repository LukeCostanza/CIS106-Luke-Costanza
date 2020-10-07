def processSize(shoeSize):
    size = shoeSize
    if size < 6:
        print("your shoe size is small!")
    else:
        if size < 9:
            print("your shoe size is medium!")
        else:
            if size < 12:
                print("your shoe size is large!")

        return size

# Main
print("What is your show size?")
size = int(input())
if size < 4:
    print("your shoe size is extra small!")
else:
    processSize(size)
