from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

k = (0, 0, 0)       #Black
g = (34, 199, 105)  #Green
b = (24, 197, 219)  #Blue
v = (180, 183, 184) #Wall
w = (255, 255, 255) #White

Level_1 = [
[v, v, v, v, v, v, v, v],
[v, k, k, k, k, b, k, v],
[v, v, v, v, v, v, k, v],
[v, k, k, k, k, k, k, v],
[v, k, v, v, v, v, v, v],
[v, k, k, k, k, k, k, v],
[v, v, v, g, k, k, k, v],
[v, v, v, v, v, v, v, v] ]


maze = Level_1
sense.set_pixels(sum(maze,[]))
x = 1
y = 1

def move_marble(x, y):
  new_x = x
  new_y = y
  for event in sense.stick.get_events():
    if event.action == "pressed":     
        if event.direction == "up":
          new_y -= 1
        elif event.direction == "down":
          new_y += 1
        elif event.direction == "left":
          new_x -= 1
        elif event.direction == "right":
          new_x += 1
        elif event.direction == "middle":
            sense.show_message("Quitter!", text_colour=[255,105,180], scroll_speed=0.05)
            sleep(2)
            exit()
        new_x, new_y = check_wall(x, y, new_x, new_y)
        print("The joystick was {} {}".format(event.action, event.direction))
        print(new_x, new_y)
  return new_x, new_y

def check_wall(x,y,new_x,new_y):
    if maze[new_y][new_x] != v:
        return new_x, new_y
    elif maze[new_y][x] != v:
        return x, new_y
    elif maze[y][new_x] != v:
        return new_x, y
    else:
        return x,y

running = True
while running:
  x, y = move_marble(x, y,)
  maze[y][x] = w
  sense.set_pixels(sum(maze,[]))
  sleep(0.05)
  maze[y][x] = k
