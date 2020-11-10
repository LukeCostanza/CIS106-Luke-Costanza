#This program informs the user which year is a leap year. 


def get_yinput():
    print("Enter a year you would like to look up: ")
    yinput = int(input())
    return yinput


def get_minput(yinput):
    minput = 1
    while minput > 0 and minput < 13:
        print("Enter a month number you would like to look up: ")
        minput = int(input())
        if minput > 0 and minput < 13:
            r = yinput % 4 
            import array as arr
            if r == 0:
                days = arr.array('i',[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) 
            else: 
                days = arr.array('i',[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
            months = ["janurary", "feburary", "march"]
            print(months [minput - 1])
            print(days [minput - 1])
 
         
def get_leap(yinput):
    r = yinput % 4 
    if r == 0:
        print ("It's a leap year!")
    else: 
        print("It's not a leap year!")


def main():
    yinput = get_yinput()
    get_leap(yinput)
    get_minput(yinput)
    print("Program end")


main()    
