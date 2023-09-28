from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

p = (255, 255, 255)
o = (0, 0, 0)

r=(255, 0, 0)
g=(0, 255, 0)
b=(0, 0, 255)

c=(0, 255, 255)
m=(255, 0, 255)
y=(255, 255, 0)
k=(0, 0, 0)
v = (180, 183, 184)

w=(255, 255, 255)

menu = [
        [o, o, o, o, o, p, o, p],
        [o, o, o, o, o, p, o, p],
        [o, o, o, o, o, p, p, p],
        [p, p, p, o, o, p, o, p],
        [p, o, o, o, o, p, o, p],
        [p, p, o, o, o, o, o, o],
        [p, o, o, o, o, o, o, o],
        [p, p, p, o, o, o, o, o]]

    
def stickmode():
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear()
    
    Level1 = [
    [v, v, v, v, v, v, v, v],
    [v, k, k, k, k, k, k, v],
    [v, k, k, k, k, k, k, v],
    [v, v, v, v, v, v, k, v],
    [v, k, k, k, k, k, k, v],
    [v, k, v, v, v, v, v, v],
    [v, k, k, g, k, k, k, v],
    [v, v, v, v, v, v, v, v]
     ]
      
    Level11 = [
    [v, v, v, v, v, v, v, v],
    [v, b, k, k, r, k, k, v],
    [v, v, k, k, k, k, k, v],
    [v, k, v, k, k, v, k, v],
    [v, r, k, k, v, k, r, v],
    [v, k, v, k, k, k, v, v],
    [v, k, g, k, v, k, k, v],
    [v, v, v, v, v, v, v, v]
     ]
    
    Level111 = [
    [v, v, v, v, v, v, v, v],
    [v, b, k, k, k, k, v, v],
    [v, v, k, v, k, k, k, v],
    [v, v, k, k, r, k, r, v],
    [v, k, r, r, k, k, k, v],
    [v, r, k, r, k, r, k, v],
    [v, k, k, g, k, r, k, v],
    [v, v, v, v, v, v, v, v]
    ]
    
    def win(win_count):
      sense.show_message("Nice!",scroll_speed=0.05)
      sleep(1)
      
      if win_count == 2:
        sense.show_message("You WON!",scroll_speed=0.05)
        main()
        
      sense.show_message("Level up!",scroll_speed=0.05)
    
      
    sense.set_pixels(sum(Level1,[]))
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
                main()
            new_x, new_y = check_wall(x, y, new_x, new_y)
            print("The joystick was {} {}".format(event.action, event.direction))
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
        
    win_count = 0
    maze = Level1
    x = 1
    y = 1
    
    running = True
    while running:
      x, y = move_marble(x, y,)
      if maze[y][x] == g:
        win(win_count)
        win_count = win_count + 1
        print("Win",win_count)
        if win_count == 1:
          maze = Level11
        if win_count == 2 :
          maze = Level111
        x = 1
        y = 1
      if maze[y][x] == r:
        sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
        main()
      maze[y][x] = b
      sense.set_pixels(sum(maze,[]))
      sleep(0.05)
      maze[y][x] = k
      
def orimode():
    from sense_hat import SenseHat
    from time import sleep
    sense = SenseHat()
    sense.clear()
    
    sense=SenseHat()
    
    r=(255, 0, 0)
    g=(0, 255, 0)
    b=(0, 0, 255)
    
    c=(0, 255, 255)
    m=(255, 0, 255)
    y=(255, 255, 0)
    k=(0, 0, 0)
    v = (180, 183, 184)
    
    w=(255, 255, 255)
    
    
    Level1 = [
    [v, v, v, v, v, v, v, v],
    [v, k, k, k, k, k, k, v],
    [v, k, k, k, k, k, k, v],
    [v, v, v, v, v, v, k, v],
    [v, k, k, k, k, k, k, v],
    [v, k, v, v, v, v, v, v],
    [v, k, k, g, k, k, k, v],
    [v, v, v, v, v, v, v, v]
     ]
      
    Level11 = [
    [v, v, v, v, v, v, v, v],
    [v, b, k, k, r, k, k, v],
    [v, v, k, k, k, k, k, v],
    [v, k, v, k, k, v, k, v],
    [v, r, k, k, v, k, r, v],
    [v, k, v, k, k, k, v, v],
    [v, k, g, k, v, k, k, v],
    [v, v, v, v, v, v, v, v]
     ]
    
    Level111 = [
    [v, v, v, v, v, v, v, v],
    [v, b, k, k, k, k, v, v],
    [v, v, k, v, k, k, k, v],
    [v, v, k, k, r, k, r, v],
    [v, k, r, r, k, k, k, v],
    [v, r, k, r, k, r, k, v],
    [v, k, k, g, k, r, k, v],
    [v, v, v, v, v, v, v, v]
    ]
    
    def win(win_count):
      sense.show_message("Nice!",scroll_speed=0.05)
      sleep(1)
      
      if win_count == 2:
        sense.show_message("You WON!",scroll_speed=0.05)
        main()
        
      sense.show_message("Level up!",scroll_speed=0.05)
    
      
    sense.set_pixels(sum(Level1,[]))
    x = 1
    y = 1
    
    def move_marble(pitch, roll, x, y):
      new_x = x
      new_y = y
      if 5 < pitch < 179 and x != 7:
        new_x -= 1
        sleep(0.05)
        for event in sense.stick.get_events():
            if event.action == "pressed":     
                if event.direction == "middle":
                    sense.show_message("Menu...", text_colour=[255,105,180], scroll_speed=0.05)
                    sleep(2)
                    main()
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
        if maze[new_y][new_x] != v:
            return new_x, new_y
        elif maze[new_y][x] != v:
            return x, new_y
        elif maze[y][new_x] != v:
            return new_x, y
        else:
            return x,y
        
    win_count = 0
    maze = Level1
    x = 1
    y = 1
    
    running = True
    while running:
      orientation = sense.get_orientation()
      pitch = round(orientation["pitch"])
      roll = round(orientation["roll"])
      x, y = move_marble(pitch, roll, x, y)
      if maze[y][x] == g:
        win(win_count)
        win_count = win_count + 1
        print("Win",win_count)
        if win_count == 1:
          maze = Level11
        if win_count == 2 :
          maze = Level111
        if maze[y][x] == r:
            sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
            main()
        x = 1
        y = 1
      if maze[y][x] == r:
        sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
        main()
      maze[y][x] = b
      sense.set_pixels(sum(maze,[]))
      sleep(0.05)
      maze[y][x] = k

def main():
    sense.set_pixels(sum(menu,[]))
    running = True
    while running:
        for event in sense.stick.get_events():
            event = sense.stick.wait_for_event()
            if event.action == "pressed":
                if event.direction == "up":
                    orimode()
                elif event.direction == "right":
                    orimode()
                elif event.direction == "down":
                    stickmode()
                elif event.direction == "left":
                    stickmode()
                elif event.direction == "middle":
                    sense.show_message("Quitting...", scroll_speed=0.05)
                    sleep(2)
                    exit()
                
main()
