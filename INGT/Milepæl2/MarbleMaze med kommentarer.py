"""
Milepæl 2

Denne koden kjører et MarbleMaze spill. På samme måte som det ekte spille hvor
man må rotere en treplate for å styre en kule gjennom en labyrint til et mål, 
har vi laget det samme, ved bruk av sensorer og et matrisebrett med LED-lys.

Koden er primært lagt slik at ved oppstart så får man to alternativer. Man kan
ta joysticken til venstre eller ned for å starte spille i "Easy-mode", der hvor
man kontrollerer ballen kun ved hjelp av joysticken, som gjør spillet på mange
måter trivielt. Man kan også ved oppstart ta joysticken til høyre eller opp for
å kjøre det i "Hard-mode". Hard-mode bruker gyroskopet og da simulerer det ekte 
spillet og er langt vanskeligere. 

Ved game-over eller game-completion så vil spille gå tilbake til hovedmenyen.
"""
from sense_hat import SenseHat #Importerer sense_hat bibliotek
from time import sleep #Importerer muligheten til en tidsstyrt delay
sense = SenseHat() #Setter utrykket sense til funksjonen SenseHat
sense.clear() #Setter LED-matrix til blank

#Fargekoder i RGB format:
p = (255, 255, 255) #Hvit
o = (0, 0, 0) #Svart eller av

r=(255, 0, 0) #Rød
g=(0, 255, 0) #Grønn
b=(0, 0, 255) #Blå

c=(0, 255, 255) #Cyan
m=(255, 0, 255) #Magenta
y=(255, 255, 0) #Gul
k=(0, 0, 0) #Av
v = (180, 183, 184) #Grå

w=(255, 255, 255) #Hvit

# Meny-matrise, med bokstaven E i nedre venstre hjørnet og bokstaven H i øvre 
# høyre hjørne
menu = [
        [o, o, o, o, o, p, o, p],
        [o, o, o, o, o, p, o, p],
        [o, o, o, o, o, p, p, p],
        [p, p, p, o, o, p, o, p],
        [p, o, o, o, o, p, o, p],
        [p, p, o, o, o, o, o, o],
        [p, o, o, o, o, o, o, o],
        [p, p, p, o, o, o, o, o]]

#Easy-mode versjonen av spillet.     
def stickmode():
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear()
    
    #Første nivå i matriseformat. Ingen hindringer til spilleren på dette 
    #nivået. Bokstavene symboliserer hvilken farge ved LED i matrisen skal være.
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
    
    #Nivå 2. Bokstaven "r" introduseres som en hindring. Er man i kontakt med
    #"r" så vil spille vise Game-over og man blir sendt til hovedmenyen
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
    
    #Nivå 3, Mange hindringer er på banen, og man må virkelig være forsiktig
    #for å ikke mislykke nivået. 
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
    
    #Funksjon for å vise hva som skjer når man fullfører nivået
    def win(win_count):
      sense.show_message("Nice!",scroll_speed=0.05)
      sleep(1)
      
      #Skjekker en win_count variabel for å determinere hvor i spillet man er
      if win_count == 2:
        sense.show_message("You WON!",scroll_speed=0.05)
        main() #Hele spille fullført, man sendes til hovedmenyen
        
      sense.show_message("Level up!",scroll_speed=0.05)
      
    sense.set_pixels(sum(Level1,[]))
    x = 1
    y = 1
    
    #Funksjon for å etablere kontrollert bevegelse, i dette tilfelle ved bruk
    #av joysticken
    def move_marble(x, y):
      new_x = x
      new_y = y
      for event in sense.stick.get_events():
        if event.action == "pressed": #Unngår dobbelinput  
            if event.direction == "up":
              new_y -= 1
            elif event.direction == "down":
              new_y += 1
            elif event.direction == "left":
              new_x -= 1
            elif event.direction == "right":
              new_x += 1
            elif event.direction == "middle": #Setter spillet til hovedmenyen
                sense.show_message("Quitter!", text_colour=[255,105,180], scroll_speed=0.05)
                sleep(2)
                main()
            new_x, new_y = check_wall(x, y, new_x, new_y) #Etablerer ulovlige begevelser
            print("The joystick was {} {}".format(event.action, event.direction)) #Print til terminal
      return new_x, new_y
    
    #Funksjon som setter veggene i labyrinten til urørlige. Slik at spilleren ikke
    #kan gå inn i veggen
    def check_wall(x,y,new_x,new_y):
        if maze[new_y][new_x] != v:
            return new_x, new_y
        elif maze[new_y][x] != v:
            return x, new_y
        elif maze[y][new_x] != v:
            return new_x, y
        else:
            return x,y
        
    win_count = 0 #Hvor mange nivåer man har klart
    maze = Level1 #Hvilke nivå man er på
    x = 1 #Spillerens posisjon
    y = 1 #Spillerens posisjon
    
    #While-løkke kjører alle funksjonene som er laget og limer hele koden sammen
    running = True #Setter en variable til True, slik at man har en senere utgang i løkken
    while running:
      x, y = move_marble(x, y,)
      if maze[y][x] == g: #Hvis spilleren er på "g" som er målet
        win(win_count)
        win_count = win_count + 1 #Iverksetter neste nivå
        print("Win",win_count)
        if win_count == 1: #Iverksetter nivå 2
          maze = Level11
        if win_count == 2 : #Iverksetter nivå 3
          maze = Level111
        x = 1
        y = 1
      if maze[y][x] == r: #Hvis spilleren er på et rødt felt
        sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
        main() #Viser game-over, og setter spilleren tilbake til hovedmenyen
      maze[y][x] = b
      sense.set_pixels(sum(maze,[]))
      sleep(0.05)
      maze[y][x] = k

#Hard-mode versjonen av spillet, som bruker gyroskopet      
def orimode():
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear()
    
    #Første nivå i matriseformat. Ingen hindringer til spilleren på dette 
    #nivået. Bokstavene symboliserer hvilken farge ved LED i matrisen skal være.
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
    
    #Nivå 2. Bokstaven "r" introduseres som en hindring. Er man i kontakt med
    #"r" så vil spille vise Game-over og man blir sendt til hovedmenyen
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
    
    #Nivå 3, Mange hindringer er på banen, og man må virkelig være forsiktig
    #for å ikke mislykke nivået. 
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
    
    #Funksjon for å vise hva som skjer når man fullfører nivået
    def win(win_count):
      sense.show_message("Nice!",scroll_speed=0.05)
      sleep(1)
      
      #Skjekker en win_count variabel for å determinere hvor i spillet man er
      if win_count == 2:
        sense.show_message("You WON!",scroll_speed=0.05)
        main() #Hele spille fullført, man sendes til hovedmenyen
        
      sense.show_message("Level up!",scroll_speed=0.05)
      
    sense.set_pixels(sum(Level1,[]))
    x = 1
    y = 1
    
    #Funksjon som bruker raspberryens orientasjon til å bestemme hvor spilleren
    #beveger seg
    def move_marble(pitch, roll, x, y):
      new_x = x
      new_y = y
      #Setter inn if-setninger for pitch og roll funksjonene til SenseHat
      if 5 < pitch < 179 and x != 7:
        new_x -= 1
        sleep(0.05)
        for event in sense.stick.get_events(): #Setter inn en "exit" ut av spillet ved bruk av joystick
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
    
    #Funksjon som setter veggene i labyrinten til urørlige. Slik at spilleren ikke
    #kan gå inn i veggen
    def check_wall(x,y,new_x,new_y):
        if maze[new_y][new_x] != v:
            return new_x, new_y
        elif maze[new_y][x] != v:
            return x, new_y
        elif maze[y][new_x] != v:
            return new_x, y
        else:
            return x,y
        
    win_count = 0 #Hvor mange nivåer man har klart
    maze = Level1 #Hvilke nivå man er på
    x = 1 #Spillerens posisjon
    y = 1 #Spillerens posisjon
    
    #While-løkke kjører alle funksjonene som er laget og limer hele koden sammen
    running = True #Setter en variabel til True, slik at man har en senere utgang i løkken
    while running:
      orientation = sense.get_orientation() #Etablerer bruk av orientasjon ved bruk av pitch og roll
      pitch = round(orientation["pitch"])
      roll = round(orientation["roll"])
      x, y = move_marble(pitch, roll, x, y)
      if maze[y][x] == g: #Hvis spilleren er på "g" som er målet
        win(win_count)
        win_count = win_count + 1 #Iverksetter neste nivå
        print("Win",win_count)
        if win_count == 1: #Iverksetter nivå 2
          maze = Level11
        if win_count == 2 : #Iverksetter nivå 3
          maze = Level111
        if maze[y][x] == r:
            sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
            main()
        x = 1
        y = 1
      if maze[y][x] == r: #Hvis spilleren er på et rødt felt
        sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05)
        main() #Viser game-over, og setter spilleren tilbake til hovedmenyen
      maze[y][x] = b
      sense.set_pixels(sum(maze,[]))
      sleep(0.05)
      maze[y][x] = k

#Hovedfunksjon. Denne kjører først ved oppstart av programmet
def main():
    sense.set_pixels(sum(menu,[])) #Setter LED-matrisen til meny-matrisen tegnet tidligere
    running = True #runnig variabel
    while running:
        for event in sense.stick.get_events():
            event = sense.stick.wait_for_event() #Ekstra event setning for å nullifisere tidligere inputs
            if event.action == "pressed":
                if event.direction == "up":
                    orimode() #Hardmode
                elif event.direction == "right":
                    orimode() #Hardmode
                elif event.direction == "down":
                    stickmode() #Easymode
                elif event.direction == "left":
                    stickmode() #Easymode
                elif event.direction == "middle": #Avslutter programmet
                    sense.show_message("Quitting...", scroll_speed=0.05)
                    sleep(2) #Gir tid til å fullføre "Quitting..." animasjonen
                    exit() #Avslutter programmet fullstendig
                
main() #Viser til at main() funksjonen skal kjøre først
