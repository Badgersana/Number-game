#Jacob Howard
#project 3
#04/11/2019

import random
from random import randint

roundCount = 0
moneySpent = 0
moneyWon = 0
selection = 0

def one_round():
    global moneyWon
    
    lowerBoundary = 0
    upperBoundary = 99
    realAnswer = randint(lowerBoundary, upperBoundary)
    i = 0
    j = 1
    jackpot = 100
    right = 10
    wrong = 5
    
    try:
        playerAnswer = int(input("Guess a number between 0 - 99: "))
        if playerAnswer >= lowerBoundary and playerAnswer <= upperBoundary:
            if realAnswer < 10:
                realAnswer = '0' + str(realAnswer)
            else:
                realAnswer = str(realAnswer)
            if playerAnswer < 10:
                playerAnswer = '0' + str(playerAnswer)
            else:
                playerAnswer = str(playerAnswer)    
            #compares player answers and finds correct thing to do
            if playerAnswer == realAnswer:
                print("Jackpot!! You win $100.")
                moneyWon = moneyWon + jackpot
                print("The correct answer was: ", int(realAnswer))
            elif realAnswer[i] == playerAnswer [j] and realAnswer[j] == playerAnswer [i]:
                print("Right digits, wrong order. You win $10")
                moneyWon = moneyWon + right
                print("The correct answer was: ", int(realAnswer))
            #check for correct numbers in wrong positions
            elif realAnswer[i] == playerAnswer[i] or realAnswer[j] == playerAnswer[j]:
                print("One correct digit and right position. You win $10")
                moneyWon = moneyWon + right
                print("The correct answer was: ", int(realAnswer))
            elif realAnswer[i] == playerAnswer[j] or realAnswer[j] == playerAnswer[i]:
                print("One correct digit and wrong position. You win $5")
                moneyWon = moneyWon + wrong
                print("The correct answer was: ", int(realAnswer))
            else:
                print("Completely wrong")
                print("The correct answer was: ", int(realAnswer))
        else:
            print("Invalid guess, number not between 0 - 99")
            one_round()
    except ValueError:
        print("Invalid guess, that was a letter not a number between 0 - 99")
        one_round()

def rule_menu():
    global selection
    
    print("===============================================================")
    print("Guessing game. $2 per round")
    print("Guess a number between 0 to 99")
    print("If perfect match, win $100")
    print("If one digit and position matches, win $10")
    print("If one digit matches with the incorrect position, win $5")
    print("Select from the menu:")
    print("---------------------------------------------------------------")
    print("1.Play")
    print("2.Check Summary")
    print("3.Exit")
    try:
        selection = int(input("Please enter your selection: "))
        if selection < 1 or selection >= 4:
            print("Invalid input")
            rule_menu()
    except ValueError:
        print("Invalid Input")
        rule_menu()
    return selection

def display_summary(roundCount, moneySpent):
    global moneyWon
    moneyMade = moneyWon - moneySpent
    print("---------------------------------------------------------------")
    print("**Your Summary**")
    print("Rounds played:", roundCount)
    print("Money spent:", "$" + str(moneySpent))
    print("Money won:", "$" + str(moneyWon))
    print("Money made:", "$" + str(moneyMade))
           

def main(roundCount, moneySpent, moneyWon):
    global selection
    running = 1
    
    while running == 1:
        rule_menu()
        if selection == 1:
            roundCount += 1
            moneySpent += 2
            one_round()
        elif selection == 2:
            display_summary(roundCount, moneySpent)
        elif selection == 3:
            display_summary(roundCount, moneySpent)
            print("Thanks for playing!")
            break

main(roundCount, moneySpent, moneyWon)




