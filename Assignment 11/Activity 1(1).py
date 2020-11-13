#This program informs the user which year is a leap year. 
#session 11 
#change variable "r"


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
            check = check_leapyear(yinput) 
            import array as arr
            if check == 0:
                days = arr.array('i',[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) 
            else: 
                days = arr.array('i',[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
            months = ["Janurary", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            print(months [minput - 1])
            print(days [minput - 1])
 
         
def get_leap(yinput):
    check = check_leapyear(yinput)
    if check == "Y":
        print ("It's a leap year!")
    else: 
        print("It's not a leap year!")


def check_leapyear(year):
    rem1 = year % 4
    rem2 = year % 100
    rem3 = year % 400
    if ((rem1 == 0) and (rem2 != 0)) or (rem3 == 0):
        answer = "Y"
    else:
        answer = "N"
    return answer


def main():
    yinput = get_yinput()
    get_leap(yinput)
    get_minput(yinput)
    print("Program end")


main()  
