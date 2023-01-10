#Copyright Skillage I.T.
#This file is Skillage I.T. software and is made available under license.
#This software is developed by: Joshua Panettieri
#Date: 15th September 2022 Time: 
#File Name: Rock_Paper_Scissors_V1.py Version: 1-0

from datetime import datetime
from tkinter import Y


class Players:
    def __init__(self, name, selection):
        self.name = name
        self.selection = selection

playmore = "y"
with open(r'C:\Users\Joshu\OneDrive\Joshua\Programming course\ICTPRG430_Apply introductory object-oriented language skills\Task 5\record.txt', 'a') as record:

    print("Welcome to our game of Rock, Paper, Scissors")
    instructions = input("Do you require instructions? y/n ")
    if instructions.lower() == "y":
        print("""Each player makes a selection, then depending on the selection made: 
        The Rock beats the Scissors, 
        The Scissors beats the Paper, 
        The Paper beats the Rock, 
        If both players make the same selection then the game is a tie""")

    while playmore.lower() == "y":
        player1 = Players(input("What is your name Player 1? "), input("What is your selection: Rock, Paper, or Scissors? "))
        player2 = Players(input("What is your name Player 2? "), input("What is your selection: Rock, Paper, or Scissors? "))        
        if player1.selection.lower() == player2.selection.lower():
            print("It's a tie!")
            record.write(str(player1.name) + " and " + str(player2.name) + " Tied " + str(datetime.now()) + '\n')
            playmore = input("Would you like to play again? y/n ")
        elif player1.selection.lower() == "rock":
            if player2.selection.lower() == "scissors":
                print("The Rock beats the Scissors! You win " + player1.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player1.name) + " Won with Rock against " + str(player2.name) + " " + str(datetime.now()) + '\n')
            else:
                print ("The Paper beats the Rock! You win " + player2.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player2.name) + " Won with Paper against " + str(player1.name) +" " + str(datetime.now()) + '\n')
        elif player1.selection.lower() == "paper":
            if player2.selection.lower() == "rock":
                print("The Paper beats the Rock! You win " + player1.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player1.name) + " Won with Paper against " + str(player2.name) +" " + str(datetime.now()) + '\n')
            else:
                print("The Scissors beats the Paper! You win " + player2.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player2.name) + " Won with Scissors against " + str(player1.name) +" " + str(datetime.now()) + '\n')
        elif player1.selection.lower() == "scissors":
            if player2.selection.lower() == "paper":
                print("The Scissors beats the Paper! You win " + player1.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player1.name) + " Won with Scissors against " + str(player2.name) +" " + str(datetime.now()) + '\n')
            else:
                print("The Rock beats the Scissors! You win " + player2.name + "! ")
                playmore = input("Would you like to play again? y/n ")
                record.write(str(player2.name) + " Won with Rock against " + str(player1.name) +" " + str(datetime.now()) + '\n')
    else:
        print("Thank you for playing, your results have been recorded.")
