# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

#Intializing global variables
RANGE=100
status=''

# helper function to start and restart the game
def new_game():
    global RANGE,n,secret_num
    secret_num=random.randrange(0, 100)
    print "New Game.Range from 0 to",RANGE
    status='NEW GAME'
    n=math.ceil(math.log(RANGE-0+1,2))
    n=int(n)
    print "You have %d guesses.\n"%n
    return RANGE

# define event handlers for control panel
def range100():
    global RANGE
    RANGE=100
    new_game()
    
def range1000():
    global RANGE
    RANGE=1000
    new_game()

def game(guess):
    global RANGE,n,status,secret_num
    print "Your guess is",guess
    

    if n>1:
        n-=1
        print "Your remaining guesses are",n
        if int(guess)<secret_num:
            print "Secret number is higher than your guess\n"
            status="Try higher"
        
        elif int(guess)>secret_num:
            print "Secret number is lower than your guess\n"
            status='Try lower'
        
        else:
            print "Correct. You win!!!\n"
            status="Correct"
            new_game()
    else:
        print "Game over. Try Again!!!\n"
        status="Game over."
        new_game()
        
   
    return status

def draw(canvas):
     canvas.draw_text(status,[70,100],20,"White")

# register event handlers for control elements and start frame       
frame=simplegui.create_frame("Guess the Number",200,200)
frame.add_button("RANGE (0-100)",range100,150)
frame.add_button("RANGE (0-1000)", range1000,150)
frame.add_input("Enter your guess:",game,150)
frame.set_draw_handler(draw)

frame.start()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
