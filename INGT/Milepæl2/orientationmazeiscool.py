#!/bin/python3

from sense_hat import SenseHat
sense = SenseHat()
event = sense.stick.wait_for_event()
sense.clear()
from time import sleep

r = (255, 0, 0)
b = (0, 0, 0)
w = (255, 255, 255)

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,b,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]
  
sense.set_pixels(sum(maze,[]))
x = 1
y = 1

def move_marble(pitch, roll, x, y):
  new_x = x
  new_y = y
  if 5 < pitch < 179 and x != 7:
    new_x -= 1
    sleep(0.05)
  elif 190 < pitch < 352 and x != 0:
    new_x += 1
    sleep(0.05)
  if 5 < roll < 179 and y != 0:
    new_y += 1
    sleep(0.05)
  elif 190 < roll < 352 and y != 7:
    new_y -= 1
    sleep(0.05)
  new_x,new_y = check_wall(x,y,new_x,new_y)
  print(pitch,roll)
  return new_x, new_y

def check_wall(x,y,new_x,new_y):
  if maze[new_y][new_x] != r:
    return new_x,new_y
  elif maze[y][new_x] != r:
    return new_x,y
  elif maze[new_y][x] != r:
    return x,new_y
  else:
    return x,y

running = True
while running == True:
  orientation = sense.get_orientation()
  pitch = round(orientation["pitch"])
  roll = round(orientation["roll"])
  x, y = move_marble(pitch, roll, x, y)
  maze[y][x] = w
  sense.set_pixels(sum(maze,[]))
  sleep(0.05)
  maze[y][x] = b
