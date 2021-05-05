import curses as cs
"""The curses module is a library to manipulate the screen inside the terminal.
"""
from random import randint
 
#We need to setup our window
cs.initscr()
win=cs.newwin(20,60,0,0)#We specify that we need 20 lines, 60 columns and starts at y=0 and x=0. (y,x)
win.keypad(1)#Allows us to use the arrow keys to control our snake
cs.noecho()#To prevent other input characters from affecting the terminal
cs.curs_set(0)#To hide curses
win.border(0)
win.nodelay(1)#Not waiting for the user input. The snakes continues to move regardless.

#snake and food
#This sets the initial coordinates of the snake
snake=[(4,10),(4,9),(4,8)]
#This sets initial coordinates for food
food=(10,20)
 
win.addch(food[0],food[1],"#")
#Game logic
score =0

ESC=27
key=cs.KEY_RIGHT#moves the snake to the right

while key != ESC:
  #endless loop.
   

  win.addstr(0,2,'Score'+ ' ' + str(score)+ ' ')
  #LIne 0 and column 2
  #This section increases the speed of the snake
  win.timeout(150 - (len(snake))//5 + len(snake)//10 % 120 )
  
  prev_key=key
  event = win.getch()
  
  if event != -1:
     key = event 
  
  else:
    prev_key

  if key not in[cs.KEY_LEFT,cs.KEY_UP,cs.KEY_RIGHT,cs.KEY_DOWN, ESC]:
    key = prev_key

  #Calculate the next snake coordinates

  y = snake[0][0]#Accessing the first tuple then the first digit in it
  x = snake[0][1]#Accessing first tuple second digit

  if key == cs.KEY_DOWN:
    
    y += 1#Cause the coordinates inc downwards frm upper corner 
  if key == cs.KEY_UP:
    
    y -= 1 
  
  if key == cs.KEY_LEFT:
    
    x -= 1
  
  if key == cs.KEY_RIGHT:
    
    x += 1


  snake.insert(0,(y,x))

  #Check if we hit the border

  if y == 0:#first line
    break
  if y == 19:#last line
    break
  if x == 0:#first column
    break
  if x == 59:#last column
    break
  #To check if snake runs over itself

  if snake[0] in snake[1:]:
    break

  if snake[0] == food:
    #We eat so score increases.
    score += 1

    food = ()
    while food == ():
      food = (randint(1,18),randint(1,58))
      if food in snake:
        food = ()
    win.addch( food[0],food[1],'#')
  else:
  #We continue to move the snake
    last = snake.pop()#This gets rid of that last * of snake's body
    win.addch(last[0],last[1]," ")


  
  win.addch(snake[0][0],snake[0][1],"*")



cs.endwin()
print(f"Final score={score}")