#Copyright Skillage I.T.
#This file is Skillage I.T. software and is made available under license.
#This software is developed by: Joshua Panettieri
#Date: 15th September 2022 Time: 
#File Name: Rock_Paper_Scissors_V2.py Version: 2-0
import random
from datetime import datetime

#Create class for players
class Players:
    def __init__(self, name, selection):
        self.name = name
        self.selection = selection

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
#Have players make their selections
    while playmore.lower() == "y":
        player1 = Players(input("What is your name Player 1? "), input("What is your selection, Choose 1 for Rock, Choose 2 for Paper, Choose 3 for Scissors or Choose 4 for Random selection? "))
        player2 = Players(input("What is your name Player 2? "), input("What is your selection, Choose 1 for Rock, Choose 2 for Paper, Choose 3 for Scissors or Choose 4 for Random selection? "))

#Winner Decision Dictionary
        winner = {
            "rock" : {"rock":"It's a tie!", "paper":"The Paper beats the Rock! "+ str(player2.name) +" wins", "scissors": "The Rock beats the Scissors! "+ str(player1.name) +" wins"},
            "paper":{"rock":"The Paper beats the Rock! "+ str(player1.name) +" wins", "paper":"It's a tie!", "scissors":"The Scissors beats the Paper! "+ str(player2.name) +" wins"},
            "scissors":{"rock":"The Rock beats the Scissors! "+ str(player2.name) +" wins", "paper":"The Scissors beats the Paper! "+ str(player1.name) +" wins", "scissors":"It's a tie!"},
            }
        
#Convert selections
        try:
            player1Choice = selectionConverter(int(player1.selection))    
            player2Choice = selectionConverter(int(player2.selection))

#Reveal and record the winner       
            print(str(player1.name + " selected " + player1Choice))
            print(str(player2.name + " selected " + player2Choice))
            print(winner[player1Choice][player2Choice])
            record.write(str(player1.name + " selected " + player1Choice)+ " " + str(player2.name + " selected " + player2Choice) +" "+ str(winner[player1Choice][player2Choice]) + " " + str(datetime.now()) +'\n')
            playmore= input("Would you like to play again? y/n ")
        except:
            print("An invalid selection was made ")
            playmore= input("Would you like to play again? y/n ")  
#Show the results    
results = input("Would you like to see the Winners records? y/n ")
if results == "y":
    record = open(r'C:\Users\Joshu\OneDrive\Joshua\Programming course\ICTPRG430_Apply introductory object-oriented language skills\Task 5\record.txt', 'r')
    print(record.read())
    print("Thank you for playing!")
else:
    print("Thank you for playing!")
