import random

userWins = 0
compWins = 0
start = int(input("Enter 1 to start game or 0 to exit: "))

def User():
    choices = ['rock','paper','scissors']
    userChoice = input("Enter Rock, Paper Or Scissors: ")
    if userChoice.lower() not in choices:
        return 0
    
    return userChoice.lower()

def CPU():
    choices = ['rock','paper','scissors']
    compChoice = random.choice(choices)
    
    return compChoice.lower()

def Logic(userWins, compWins, start):
    if(start == 0):
        return 'Ok, goodbye!'
    while(True):
        computer = CPU()
        person = User()
        if(computer=='rock' and person == 'scissors' or computer == 'scissors' < person == 'paper' or computer == 'paper' < person == 'rock'):
            print(f"Computer chose {computer}")
            print("The computer won!")
            compWins+=1
        elif(person == 'rock' and computer == 'scissors' or person == 'scissors' and computer == 'paper' or person == 'paper' and computer == 'rock'):
            print(f"Computer chose {computer}")
            print("You won!")
            userWins+=1
        elif person == 0:
            print("Didn't understand")
        else:
            print("Tie game, nobody gets a point!")    
        answer = playAgain()
        if(answer == 'no'):
            break
        elif(answer=='yes'):
            print("Alright, continue!")
        else:
            return "Don't understand. Erasing all progress from this session"

    if(userWins > compWins):
        return f"You won with {userWins} point/s!"
    elif(userWins <  compWins):
        return f"The computer won with {compWins} point/s!"
    else:
        return f"Tie Game with {compWins} point/s!"    

def playAgain():
    play_again = input("Would you like to continue? ")
    return play_again.lower()



print(Logic(userWins, compWins, start))

