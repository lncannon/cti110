# CTI-110 
# M5HW1 - Distance Traveled  
# Lisa Cannon
#26NOV17
# Calculating the distance traveled by a car.

#Get speed and hours from user
speed = int(input('What is the speed of the vehicle in mph?'))
time = int(input('How many hours has it traveled?'))

print('Hours \t Distance Traveled')
print('-----------------------------------------------')

#Calculate the distance traveled and display in a table

for time in range(1, 1 + time):
        distance = speed * time
        print(time, '\t', distance,'miles')
#THE END :)



