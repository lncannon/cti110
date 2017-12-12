# A guessing game. Program will select a random number for user to guess
# 10DEC17
# CTI-110 M6HW2 - Random Number Guessing Game
# Lisa Cannon
#

def play_game():
    import random

    #guessesTaken = 0
    secretNumber = random.randint(1, 100)
                                  
    
    guess = int(input('Enter an number from 1 to 100: '))

    while secretNumber != guess:
        #guessesTaken = guessesTaken + 1
                   
        if guess < secretNumber:
            print('Too low, try again.')
            guess = int(input('Enter another number from 1 to 100: '))
            
        elif guess > secretNumber:
            print('Too high, try again')
            guess = int(input('Enter another number from 1 to 100: '))

        else:
            break

    
def main():
    playAgain = 'Y'
    while (playAgain.upper() == 'Y'):
        play_game()
        print('Congratulations! You are correct.')
        playAgain = (input('If you would like to play again please enter Y for Yes.'))
               
main()
