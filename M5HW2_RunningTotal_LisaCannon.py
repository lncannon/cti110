# CTI-110 
# M5HW2 - Running Total
# Lisa Cannon
#26NOV17
# Calculating a running total

total = 0

while True:
        newNumber = int(input("Enter a number:"))
        total = total + newNumber
        if newNumber < 0:
                break

print("Running Total:", total)

#the end :)



