#Nabil Yasser
#Python3~

#COLORS#
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
try:
    shell = sys.stdout.shell
except AttributeError:
    raise RuntimeError("you must run this program in IDLE")

import random

def RESTART():
    print("")
    shell.write("HEY! WELCOME TO MY GAME! In this game you will have to guess a number from","BLACK")
    shell.write(" 0 ","COMMENT")
    shell.write("to","BLACK")
    shell.write(" 100 ","COMMENT")
    shell.write("in less than 5 Guesses!\n","BLACK")
    random_number = random.randint(0, 100)
    #print(random_number)
                                  #information#
    Numbers_list = []
    guesses = 0
    possibilities = [int(1), int(2), int(3)]
    print("First, What difficulty do you want to choose?")                  
    print("Choose a difficulty:    1   -   2   -  3\n                       Easy - Normal - Hard")
    Y = input("Choose the number: ")
    while Y.isdigit() == False or int(Y) not in possibilities:
        print("Please choose a number from the choices")
        Y = input("Choose the number: ")
    if int(Y) == 1:
        guesses = 12
    elif int(Y) == 2:
        guesses = 6
    elif int(Y) == 3:
        guesses = 3
    #You have X guesses
    shell.write("Number of Guesses you Have: ","STRING")
    print(guesses)
    Guess_Number = input("Guess Number: ")
    while guesses > 0:
        while Guess_Number.isdigit() == False:
            shell.write("That's not a number!","COMMENT")
            print("")
            Guess_Number = input("ReGuess a Number: ")
        if int(Guess_Number) == random_number:
            print("")
            shell.write("You Won ! CONGRATULATION. Your score is: ","STRING")
            if int(Y) == 1:
                points = int(guesses) * 10
            if int(Y) == 2:
                points = int(guesses) * 25
            if int(Y) == 3:
                points = int(guesses) * 50
            print(points)
            RE= input("Write 'Y' for another game and any button to stop: ")
            if RE == "Y" or RE == "y":
                RESTART()
            else:
                shell.write("Have a good day!","KURO")
                break
        #Number repeated        
        while Guess_Number in Numbers_list:
            print("\nYou already Writed that. You still have",guesses,"Guesses")
            Guess_Number = input("Guess Number: ")
        #Out of range    
        while int(Guess_Number) > 100 or int(Guess_Number) < 0:
            print("")
            shell.write("It is out of the Range!!!\n","COMMENT")
            shell.write("You still have ","Kuro")
            print(guesses,"Guesses.\n")
            Guess_Number = input("Guess Number: ")
        #Number more than random 
        if int(Guess_Number) > random_number:
            Numbers_list = Numbers_list
            Numbers_list.append(Guess_Number)
            print("              ")
            shell.write("Less!","hit")
            guesses -= 1
            shell.write("\nThe number of Guesses you still have: ","COMMENT")
            print(guesses,"\n")
            if guesses > 0:
                Guess_Number = input("Guess Number: ")
        #Number less than random        
        elif int(Guess_Number) < random_number :
            Numbers_list = Numbers_list
            Numbers_list.append(Guess_Number)
            print("              ")
            shell.write("More!","hit")
            guesses -= 1
            print("")
            shell.write("The number of Guesses you still have: ","COMMENT")
            print(guesses,"\n")
            if guesses > 0:
                Guess_Number = input("Guess Number: ")
    if guesses == 0:
        print("")
        shell.write("Game OVER !!!","ERROR")
        shell.write(" Almost!","COMMENT")
        print("")
        shell.write("The number was ","BLACK")
        print(random_number)
        print("")
        shell.write("Write ","KEYWORD")
        shell.write("'Y'","STRING")
        shell.write(" for another game or just Press ","KEYWORD")
        shell.write("enter","COMMENT")
        shell.write(" to stop: ","KEYWORD")
        RE= input("")
        if RE == "Y" or RE == "y":
            RESTART()
        else:
            print("")
            shell.write("Have a good day!","KURO")       
RESTART()
