#Lisa Cannon
#CTI 110
#M6HW1 - Test Average and Grades
#9DEC17
#Program will calclate test average and assign a letter grade


def calAverage(testOne, testTwo, testThree, testFour, testFive):
    average = (testOne + testTwo + testThree + testFour + testFive) / 5
    return average

#assign letter grade
def determineGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'C'
    else:
        return 'F'

#enter test grade
def main():
    
    testOne = float(input("Enter test grade 1:"))
    letterOne = determineGrade(testOne)
    testTwo = float(input("Enter test grade 2:"))
    letterTwo = determineGrade(testTwo)
    testThree = float(input("Enter test grade 3:"))
    letterThree = determineGrade(testThree)
    testFour = float(input("Enter test grade 4:"))
    letterFour = determineGrade(testFour)
    testFive = float(input("Enter test grade 5:"))
    letterFive = determineGrade(testFive)

    #grade = determineGrade(testOne, testTwo, testThree, testFour, testFive)

    print('Test 1 = ', letterOne)
    print('Test 2 = ', letterTwo)
    print('Test 3 = ', letterThree)
    print('Test 4 = ', letterFour)
    print('Test 5 = ', letterFive)
    average = calAverage(testOne, testTwo, testThree, testFour, testFive)
    print('Your overall test average is ', (average))

main()
