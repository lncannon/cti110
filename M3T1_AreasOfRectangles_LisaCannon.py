# Lisa Cannon
# CTI-110
# M3T1: Areas of Recatangles
# 24SEP17

print ("This program will calculate the area of two rectangles.")

# Rectangle One
width1 = int(input("Enter the width of Rectangle One: "))
height1 = int(input("Enter the  of Rectangle One: "))

area1 = width1 * height1
##print ("The area of Rectangle One is:", area1)

# Rectangle Two

width2 = int(input("Enter the width of Rectangle Two: "))
height2 = int(input("Enter the  of Rectangle Two: "))

area2 = width2 * height2
##print ("The area of Rectangle One is:", area2

if area1 > area2:
    area = "Rectangle One has the greatest area."
elif area1 < area2:
    area = "Rectangle Two has the greatest area."
elif area1 is area2:
    area = "The Rectangles have equal areas"

print (area)

    
