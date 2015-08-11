#! /usr/bin/env python
# A simple rock, paper, scissors game.

import random

numOfGames = 0
computerWins = 0
playerWins = 0
tieGames = 0

def checkMove(player):
    possibleMoves = ["rock", "paper", "scissors"]
    if player.lower() in possibleMoves:
        return True
    else:
        return False

def randomComputerMove():
    randomInt = random.randint(1,9)
    if randomInt <= 3:
        return "rock"
    elif randomInt > 3 and randomInt <= 6:
        return "paper"
    elif randomInt > 6:
        return "scissors"

def compareMoves(player, computer):
    global tieGames
    global playerWins
    global computerWins

    if player == computer:
        tieGames += 1
        return "Tie!"
    if player == "rock":
        if computer == "scissors":
            playerWins += 1
            return "You win!"
        elif computer == "paper":
            computerWins += 1
            return "You lose."
    elif player == "paper":
        if computer == "rock":
            
            playerWins += 1
            return "You win!"
        elif computer == "scissors":
            computerWins += 1
            return "You lose."
    elif player == "scissors":
        if computer == "paper":
            playerWins += 1
            return "You win!"
        elif computer == "rock":
            computerWins += 1
            return "You lose."

def displayGameStats():
    print("Win: %6.2f%% Loss: %6.2f%% Tie: %6.2f%%" % 
          (playerWins/numOfGames*100,
           computerWins/numOfGames*100,
           tieGames/numOfGames*100))
    
while(True):
    playerMove = input("Enter a move: ")
    if (playerMove == "q" or playerMove == "quit"):
        break

    if checkMove(playerMove) == False:
        print("Invalid move. Try again.\n")
        continue

    numOfGames += 1
    compMove = randomComputerMove()
    outcome = compareMoves(playerMove.lower(), compMove)

    print("You played %s" % playerMove)
    print("Computer played %s" % compMove)
    print("%s\n" % outcome)

print("\nThank you for playing!\n")

if numOfGames > 0:
    print("Game stats: ")
    displayGameStats()
