
import time
print("Hello and welcome to a beginner hangman Python project.")
time.sleep(3)

name = input("What is your name ? \n").title()
if name == "Carlos":
    print("dame un beso antes de empezar :D")
else:
    print("Welcome", end=" ")

time.sleep(2)
welcome = input(name + ", would you like to try the game ? \n y/n \n")
print("Analazing..")
time.sleep(1)
if welcome == "y":
    print("That is great.")
else:
    print("Do you even have the choice ?")

time.sleep(2)
#secret word is a spell in Hogwards Legacy
secret_word = "imperio"

# depending on the word length, the player has either 5 turns or 10
if len(secret_word) <= 6:
    turns = 5
else:
    turns = 10

time.sleep(1)
print("You start with ", turns, " chances. Every time you get answer wrong, you will have less chances to guess the word.")
time.sleep(3)
print("Write \"quit\" to stop the game.")
time.sleep(1)
#the player can guess with this variable
guesses = ""

while turns > 0:
    fail = 0
    
    for letter in secret_word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print(" - ", end=" ")
            fail += 1
    if fail == 0:
        print("You have won this round")
        break
    
    guess = input("\n Guess one letter please. \n")
    print("Analyzing..")
    time.sleep(2)
    if guess == "quit":
        print("OK, bye bye")
        quit()
    
    guesses += guess
    if guess not in secret_word:
        turns -= 1
        time.sleep(2)
        print("\n Wrong!")
        time.sleep(1)
        print("\n You have ", turns, " left. Keep at it. \n")
        if turns == 0:
            print("\n You have lost")
    






















"""
#importing the time module
import time

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here we set the secret. You can select any word to play with. 
word = ("secret")

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash
            print ("_",end=""),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")
    # exit the script
        break            
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose"  )
"""