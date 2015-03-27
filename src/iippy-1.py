# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

global num_guess , num_secret , num_remain , num_range1 ,num_range2


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here  
    pass

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_guess , num_secret , num_remain , num_range1 ,num_range2
    num_secret = random.randint(0, 100) 
    num_range1 = 0 
    num_range2 = 100
    num_remain = 7
    print "New game.Range is from 0 to 100"
    
    print "Number of remaining guesses is", num_remain
   
   
    return num_remain
  
    
    
    
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_guess , num_secret , num_remain , num_range1 ,num_range2
    num_secret = random.randint(0, 1000)
    num_range1 = 0 
    num_range2 = 1000
    num_remain = 10
    print "New game.Range is from 0 to 1000"
    
    print "Number of remaining guesses is", num_remain
    
    
    return num_remain
    
def input_guess(guess):
    # main game logic goes here	
    global num_guess , num_remain , num_range1 ,num_range2
    num_guess = int(guess)
    print "Guess was" , guess
    num_remain -=1 
    print "Number of remaining guesses is", num_remain
    if num_remain >= 0:
            if num_guess == num_secret:
                print "Correct!"
            elif num_range1 < num_guess < num_secret:
                print "Higher!"
                num_range1 = num_guess
            elif num_secret < num_guess < num_range2:
                print "Lower!"
                num_range2 = num_guess
            else:     
                print "The wrong number!"     
    else:
            print "Game over!"
    return num_remain
    return num_guess

    
# create frame
f = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100 )",range100, 200)
f.add_button("Range is [0,1000 )",range1000, 200)
f.add_input("Enter a guess",input_guess , 200)



# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
