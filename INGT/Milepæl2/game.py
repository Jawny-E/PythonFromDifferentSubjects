"""
Milepæl 2
Denne koden kjører et MarbleMaze spill. På samme måte som det ekte spille hvor
man må rotere en treplate for å styre en kule gjennom en labyrint til et mål, 
har vi laget det samme, ved bruk av sensorer og et matrisebrett med LED-lys.
Koden er primært lagt slik at ved oppstart så får man to alternativer. Man kan
ta joysticken til venstre for å starte spille i "Easy-mode", der hvor
man kontrollerer ballen kun ved hjelp av joysticken, som gjør spillet på mange
måter trivielt. Man kan også ved oppstart ta joysticken til høyre for
å kjøre det i "Hard-mode". Hard-mode bruker gyroskopet og da simulerer det ekte 
spillet og er langt vanskeligere. 
Ved game-over eller game-completion så vil spille gå tilbake til hovedmenyen.
"""
from sense_hat import SenseHat #Importerer sense_hat bibliotek
from time import sleep #Importerer muligheten til en tidsstyrt delay
from timeit import default_timer as timer
import csv #Importerer csv for å logge vinnerene
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

path = "/home/e_johnsen/scores.csv" #Dette er filplasseringa til resultata, denne kan endrast for eigen bruk

#Desse led-menyane visast 3-gonger mellom kvart spel for å friske opp minnet til spelaren
menu1 = [
        [o, o, o, o, o, o, o, o],
        [o, o, o, o, o, o, o, o],
        [p, p, p, o, o, p, o, p],
        [p, o, o, o, o, p, o, p],
        [p, p, o, o, o, p, p, p],
        [p, o, o, o, o, p, o, p],
        [p, p, p, o, o, p, o, p],
        [o, o, o, o, o, o, o, o]] #Viser E, for easy til venstre, og H for Hard til høgre
menu2= [
        [o, p, o, p, o, o, o, o],
        [o, p, p, p, o, o, o, o],
        [o, p, o, p, o, p, p, p],
        [o, o, o, o, o, p, o, o],
        [o, o, o, o, o, p, p, p],
        [o, p, o, o, o, o, o, p],
        [o, p, o, o, o, p, p, p],
        [o, p, p, p, o, o, o, o]] #Viser H oppe og L nede, med ein S på sida. Dette står for High Score og Lowest score 

#Easy-mode versjonen av spillet.     
def stickmode():
    start = timer()#Starer timeren, som er scoren
    
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
      sense.show_message("Nice!",scroll_speed=0.05) #Viser hver gang man vinner
      sleep(1)
      
      #Skjekker en win_count variabel for å determinere hvor i spillet man er
      if win_count == 2:
        sense.show_message("You WON!",scroll_speed=0.05)
        write_score(timer()-start, "E") #Bruker funksjonen write_score for å legge resultatet til csv filen
        main() #Hele spille fullført, man sendes til hovedmenyen
        
      sense.show_message("Level up!",scroll_speed=0.05)#Denne viser dersom spillet ikke er fullført
      
    
    #Funksjon for å etablere kontrollert bevegelse, i dette tilfelle ved bruk
    #av joysticken
    def move_marble(x, y):
      new_x = x
      new_y = y
      for event in sense.stick.get_events():
        if event.action == "pressed": #Unngår dobbelinput  
            if event.direction == "up": #Flytt kula opp, y må minske med 1
              new_y -= 1
            elif event.direction == "down": #Y må øke med 1 for å flytte ned
              new_y += 1
            elif event.direction == "left": #x må minke med 1 for å flytte til venstre
              new_x -= 1
            elif event.direction == "right": #x må øke med 1 for å flytte til høgre
              new_x += 1
            elif event.direction == "middle": #Setter spillet til hovedmenyen dersom spilleren klikker ned
                sense.show_message("Quiting!", text_colour=[255,105,180], scroll_speed=0.05)
                sleep(2)
                main()
            new_x, new_y = check_wall(x, y, new_x, new_y) #Stopper ulovlige begevelser
            print("The joystick was {} {}".format(event.action, event.direction)) #Printer input til terminal
      return new_x, new_y
    
    #Funksjon som setter veggene i labyrinten til urørlige. Slik at spilleren ikke
    #kan gå inn i veggen
    def check_wall(x,y,new_x,new_y):
        if maze[new_y][new_x] != v:
            return new_x, new_y #Dersom de nye x og y verdiene ikke er lik en vegg kan de kjørest
        elif maze[new_y][x] != v:
            return x, new_y #Dersom man kræsjer med veggen med x-verdi, blir kunn y-verdi oppdatert
        elif maze[y][new_x] != v:
            return new_x, y #Dersom man kræsjer med veggen med y-verdi, blir kunn x-verdi oppdatert
        else:
            return x,y #Dersom begge verdiene kræsjer blir ingenting oppdatert
    
    #Nå starter vi å kjøre programmet!!
    
    sense.set_pixels(sum(Level1,[])) #Setter på startlevelen manuellt    
    win_count = 0 #Hvor mange nivåer man har klart
    maze = Level1 #Hvilke nivå man er på
    x = 1 #Spillerens start posisjon
    y = 1 #Spillerens start posisjon
    
    
    running = True #Setter en variable til True, slik at man har en senere utgang i løkken
    #While-løkke kjører alle funksjonene som er laget og limer hele koden sammen
    while running:
      x, y = move_marble(x, y,)
      
      #Når man kommer fram til grønt merke skjer dette:
      if maze[y][x] == g: #Hvis spilleren er på "g" som er målet 
        win(win_count)
        win_count = win_count + 1 #Teller hvor mange nivå man har vunnet
        print("Win",win_count) #Skriver til konsollen hvor mange nivå man har vunnet
        
        if win_count == 1: #Iverksetter nivå 2
          maze = Level11
        if win_count == 2 : #Iverksetter nivå 3
          maze = Level111
        x = 1 #Setter spilleren tilbake til startposisjon
        y = 1
      
     #Dersom man lander på rødt felt skjer dette:
      if maze[y][x] == r: #Sjekker om spilleren er på et rødt felt
        sense.show_message("Game Over", text_colour=[255,105,180], scroll_speed=0.05) #Viser game over
        sleep(1) #Venter litt
        main() #Setter spilleren tilbake til hovedmenyen
      
      maze[y][x] = b #Flytter spillerbrikken, og oppdaterer led-matrisen
      sense.set_pixels(sum(maze,[]))
      
      sleep(0.05)
      maze[y][x] = k #Fjerner den forrige posisjonen til spiller-brikka

#Hard-mode versjonen av spillet, som bruker gyroskopet      
def orimode():
    from sense_hat import SenseHat
    sense = SenseHat()
    sense.clear() #Fjerner alt som har vært i led-matrisa
    start = timer() #Starer timeren, som er scoren
    
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
        write_score(timer()-start, "H")
        main() #Hele spille fullført, man sendes til hovedmenyen
        
      sense.show_message("Level up!",scroll_speed=0.05)
      
    
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
    
    #HER STARTER PROGRAMMET!
    
    sense.set_pixels(sum(Level1,[])) #Setter på startlevelen
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
      
      maze[y][x] = b #flytter spillebrikken
      sense.set_pixels(sum(maze,[])) #Oppdaterer led-matrisen
      sleep(0.05)
      maze[y][x] = k #skrur av led for den forrige posisjonen



#Denne funksjonen skal skrive inn alle vinnerresultata i ei csv fil
def write_score(input, game_mode):
    game_count = 0
    fil = open(path,"r")
    _x = fil.readline()
    while _x != "":
        game_count += 1
        _x = fil.readline() #Denne løkka går gjennom csv fila og ser kor mange spill som er registrert
    fil.close()
    
    with open(path, "a") as fil:
        writer = csv.writer(fil, delimiter=';')
        writer.writerow(["Dato",str(game_count),round(input, 2), str(game_mode)])
        #Skriver inn dato(mangler), hvilket nummer spillet ditt er i listen, scoren(tid) og modus

        
#Denne funksjonen skal sortere vinner-resultata i ei liste
def highscore():
    scores = [] #Denne lista skal vi fylle med resultat(tid)
    fil = open(path,"r")
    _x = fil.readline() #Leser av første linje, denne skal ikkje være med
    _x = fil.readline()
    
    while _x != "": #Fortsetter til linjen er tom
        _x = _x.split(";") #Splitter linjen slik at vi kan hente ut tiden som er
        scores.append(_x[2]) #I posisjon 2 og legger dette inn i listen
        _x = fil.readline()
    fil.close() #Lukker filen
    scores.sort() #Sorterer listen, dette blir som standard gjort i stigende rekkefølge
    return(scores) #Returnerer listen

    
#Hovedfunksjon. Denne kjører først ved oppstart av programmet
def main():
    i = 0
    for i in range(3): #Kjører en kort oppfriskning av bruk av menyen, her med symbol
        sense.set_pixels(sum(menu1,[])) #Vis 
        sleep(1)
        sense.set_pixels(sum(menu2,[]))
        sleep(1)
        i +=1
    sense.show_letter("R", text_colour=r) #Viser bokstaven R, for å vise at programmet er klar til å kjøre
    running = True #running variabel, for å senere kunne stoppe loopen
    while running:
        for event in sense.stick.get_events():
            event = sense.stick.wait_for_event() #Ekstra event setning for å nullifisere tidligere inputs
            if event.action == "pressed": #Dersom joy-stick opp: Finn high score
                if event.direction == "up":
                    hs = highscore() #Bruker high score funksjonen
                    hs = hs[0] #Henter ut posisjon 0 fra listen (kortest tid)
                    sense.show_message(str(hs) + " s") #viser resultatet i sekund
                    sleep(1)
                    main() #starter main på nytt
                elif event.direction == "right": #Hardmode
                    orimode()
                elif event.direction == "down": #Dersom joy-stick ned: Finn low score
                    ls = highscore()
                    ls = str(ls[-1]) #henter ut posisjon -1 fra listen, høyeste tall
                    sense.show_message(str(ls) + " s") #Viser resultatet i sekund
                    sleep(1)
                    main() #starter main på nytt
                elif event.direction == "left":#Easymode
                    stickmode() 
                elif event.direction == "middle": #Avslutter programmet, når joystick blir klikket inn
                    sense.show_message("Quitting...", scroll_speed=0.05)
                    sleep(2) #Gir tid til å fullføre "Quitting..." animasjonen
                    exit() #Avslutter programmet fullstendig
            
#Når vi starter programmet kommer en detaljert melding om bruk av menyen
sense.show_message("Opp: HS, Ned: LS, Hoegre: Hard, Venstre: Easy", scroll_speed=0.05, text_colour=c)
sleep(2)
main() #Viser til at main() funksjonen skal kjøre først
