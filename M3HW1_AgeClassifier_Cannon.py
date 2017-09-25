# CTI-110 
# M3HW1 - Age Classifier 
# Lisa Cannon
# 24SEP17


def main():
    # Program to determine a person's stage in life based off age

    infant = 1
    child = 13
    teenager = 20
    adult = 21

    age = int(input('Enter age: '))

    if age <= infant:
        print ('You are an Infant')
##
    if age <= child:
        print ('You are a Child.')

    elif age <= teenager:
        print ('You are a Teenager.')

    elif age >= adult:
        print ('You are an Adult.')
        
# program start
main ()
