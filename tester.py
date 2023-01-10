#Copyright Skillage I.T.
#This file is Skillage I.T. software and is made available under license.
#This software is developed by: Joshua Panettieri
#Date: 15th September 2022 Time: 
#File Name: Rock_Paper_Scissors_V2.py Version: 2-0
import random
from datetime import datetime

#Create class for players
class Players:
    def __init__(self, firstName, lastName, rounds, selection):
        self.firstName = firstName
        self.lastName = lastName
        self.rounds = rounds
        self.selection = selection

class Selection:
    def __init__(self,type, win, lose, tie):
        self.type = type
        self.win = win
        self.lose = lose
        self.tie = tie        

#Convert number choice to string
def selectionConverter(number):
    if number == 4:
        number = randomCalculation
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"
    
#Set variables
randomCalculation = random.randint(1,3)
playmore = "y"
roundCounter = 1
rock = Selection ("rock", "scissors", "paper", "rock")
paper = Selection ("paper", "rock", "scissors", "paper")
scissors = Selection("scissors", "paper", "rock", "scissors")

#Open or create a file for the results to be stored
with open(r'C:\Users\Joshu\OneDrive\Joshua\Programming course\ICTPRG430_Apply introductory object-oriented language skills\Task 5\record.txt', 'a') as record:

#Check if the player needs instructions
    print("Welcome to our game of Rock, Paper, Scissors")
    instructions = input("Do you require instructions? y/n ")
    if instructions.lower() == "y":
        print("""Each player makes a selection, then depending on the selection made: 
        The Rock beats the Scissors, 
        The Scissors beats the Paper, 
        The Paper beats the Rock, 
        If both players make the same selection then the game is a tie""")

#Main loop
#Find out the player details    
    player1 = Players(input("What is your First name Player 1? "), input("What is your Last name Player 1? "), input("How many rounds do you want to play? "), "")
    player2 = Players(input("What is your First name Player 2? "), input("What is your Last name Player 2? "), player1.rounds, "")
#Start game loop
    while roundCounter <= int(player1.rounds):
#Have players make their selections
        player1 = Players(player1.firstName, player1.lastName, player1.rounds, input(str(player1.firstName) + " What is your selection, Choose 1 for Rock, Choose 2 for Paper, Choose 3 for Scissors or Choose 4 for Random selection? "))
        player2 = Players(player2.firstName, player2.lastName, player1.rounds, input(str(player2.firstName) + " What is your selection, Choose 1 for Rock, Choose 2 for Paper, Choose 3 for Scissors or Choose 4 for Random selection? "))
#Winner Decision Dictionary
        winner = {
            rock.type : {rock.tie:"It's a tie!", rock.lose:"The Paper beats the Rock! "+ str(player2.firstName) +" wins", rock.win: "The Rock beats the Scissors! "+ str(player1.firstName) +" wins"},
            paper.type :{paper.win:"The Paper beats the Rock! "+ str(player1.firstName) +" wins", paper.tie:"It's a tie!", paper.lose :"The Scissors beats the Paper! "+ str(player2.firstName) +" wins"},
            scissors.type:{scissors.lose:"The Rock beats the Scissors! "+ str(player2.firstName) +" wins", scissors.win:"The Scissors beats the Paper! "+ str(player1.firstName) +" wins", scissors.tie:"It's a tie!"},
            }
        
#Convert selections
        try:
            player1Choice = selectionConverter(int(player1.selection))    
            player2Choice = selectionConverter(int(player2.selection))

#Reveal and record the winner       
            print(str(player1.firstName + " selected " + player1Choice))
            print(str(player2.firstName + " selected " + player2Choice))
            print(winner[player1Choice][player2Choice])
            record.write("In round " + str(roundCounter) +" " + str(player1.firstName) +" " + str(player1.lastName) + " selected " + str(player1Choice)+ " " + str(player2.firstName) +" "+ str(player2.lastName) + " selected " + str(player2Choice) +" "+ str(winner[player1Choice][player2Choice]) + " " + str(datetime.now()) +'\n')
            roundCounter = roundCounter + 1
        except:
            print("An invalid selection was made, try again.")
#Show the results    
results = input("Would you like to see the Winners records? y/n ")
if results == "y":
    record = open(r'C:\Users\Joshu\OneDrive\Joshua\Programming course\ICTPRG430_Apply introductory object-oriented language skills\Task 5\record.txt', 'r')
    print(record.read())
    print("Thank you for playing!")
else:
    print("Thank you for playing!")
