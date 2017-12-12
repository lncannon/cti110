#Lisa Cannon
#CTI 110
#M6T2 - Feet to Inches Converter
#10DEC17
#Program to convert feet to inches

def feet_to_inches():
    feet = input('Please enter the distance in feet:')
    inches = feet * 12
    return inches


def main():
    inches = feet_to_inches()
    print('The distance is ',inches, ' inches')


main()
