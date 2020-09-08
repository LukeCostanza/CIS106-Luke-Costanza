#This program displays the gross pay of an hourly worker
Hours=int(input("Hours "))
Rate=int(input("Rate "))
Weekly=(int(Hours*Rate))
Monthly=(Weekly*4.33)
Anually=(Monthly*12)
print("your pay this Week is $" + str(Weekly))
print("your pay this Month is $" + str(Monthly))
print("your pay this Year is $" + str(Anually))
