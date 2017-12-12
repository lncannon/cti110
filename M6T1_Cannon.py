#Lisa Cannon
#CTI 110
#M6T1 - Kilometer Converter
#10DEC17
#Program converts Kilometers to Miles

def show_miles(kilometers):
    miles = kilometers * 0.6214
    return miles

def main():
    kilometers = int(input('Please enter the number of Kilometers you would like to convert to miles:'))
    miles = show_miles(kilometers)
    print(kilometers, ' kilometers is equal to ', miles, 'miles.')

main()


