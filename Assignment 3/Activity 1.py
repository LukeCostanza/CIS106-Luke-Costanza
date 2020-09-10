# This program displays the gross pay of an hourly worker.

hours = int(input("Hours "))
rate = int(input("Rate "))

weekly = hours * rate
monthly = weekly * 4.33
annually = monthly * 12

print("your pay this Week is $" + str(weekly))
print("your pay this Month is $" + str(monthly))
print("your pay this Year is $" + str(annually))
