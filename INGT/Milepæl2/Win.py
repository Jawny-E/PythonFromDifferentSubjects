#!bin/bin/python3

from sense_hat import SenseHat
from random import choice
from time import sleep

sense=SenseHat()
sense.set_rotation(270)

r=(255, 0, 0)
g=(0, 255, 0)
b=(0, 0, 255)

c=(0, 255, 255)
m=(255, 0, 255)
y=(255, 255, 0)
k=(0, 0, 0)
v = (180, 183, 184)

w=(255, 255, 255)

available_colors =[r, g, b, c, m, y, w] 

random_color = choice(available_colors)

Level1 = [
v, v, v, v, v, v, v, v,
v, b, k, k, k, k, k, v,
v, k, k, k, k, b, k, v,
v, v, v, v, v, v, k, v,
v, k, k, k, k, k, k, v,
v, k, v, v, v, v, v, v,
v, k, k, k, k, k, k, v,
v, v, v, g, k, k, k, v,
 ]
  
Level11 = [
v, v, v, v, v, v, v, v,
v, v, k, k, k, k, k, v,
v, v, k, k, k, b, k, v,
v, k, v, k, k, v, k, v,
v, k, k, k, v, k, k, v,
v, k, v, k, k, k, v, v,
v, k, g, k, v, k, k, v,
v, k, v, k, k, k, k, v,
 ]

Level111 = [
v, v, k, v, k, b, k, k,
k, k, k, k, k, k, v, v,
v, v, k, v, k, k, k, k,
k, k, k, k, k, b, v, v,
k, k, v, v, k, k, k, k,
k, k, k, v, k, v, v, v,
v, k, k, k, k, k, k, k,
v, k, v, v, v, v, v, k,
]

  
def win(win_count):
  sense.show_message("Nice!",scroll_speed=0.05)
  sleep(1)
  
  if win_count == 2:
    sense.show_message("You WON!",scroll_speed=0.05)
    exit()
    
  sense.show_message("Level up!",scroll_speed=0.05)

def next_lvl(level):
  
  sense.set_pixels(level)
  
  
  
  
  
game_over = False
win_count = 0

sense.set_pixels(Level1)
sleep(2)

while game_over == False:
  win(win_count)
  win_count = win_count + 1
  print("Win",win_count)
  if win_count == 1:
    sense.set_pixels(Level11)
    sleep(3)
  if win_count == 2:
    sense.set_pixels(Level111)
    sleep(3)
  sleep(3)
