"""
Milepael 0 av Claus Berg, Martine Karlson, Kevin Johansen, Julie Tufta og Ellen Johnsen, alle har laga kvar sin funksjon(inkl. main)
Gruppe 1
"""
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

#Fargane tilgjengleg i prosjektet, raud(rosa), grønn, blå, cyan, mangenta, gul, svart og kvitt
r = [255, 102, 102]
g = [77, 212, 126]
b = [100, 176, 240]

c = [0, 255, 255]
m = [255, 0, 255]
y = [255, 255, 0]

black = [0,0,0]
k= [100,100,100]

#Dette smilefjeset viser når raspberrien er klar for ny input
idle = [
  black,black,b,black,black,b,black,black,
  black,black,b,black,black,b,black,black,
  black,black,b,black,black,b,black,black,
  black,black,black,black,black,black,black,black,
  black,black,black,black,black,black,black,black,
  black,b,black,black,black,black,b,black,
  black,b,black,black,black,black,b,black,
  black,b,b,b,b,b,b,black,
 ]

""""
    føremålet med funksjonen er at skjermen oppdaterast og roterast slik at pila alltid viser retningen "ned"
    dette er ein flott måte å teste ut akselerometeret på senseHat
""""
def fun_1():
    arrow = [
    k, k, k, r, r, k, k, k,
    k, k, k, k, r, r, k, k,
    k, k, k, k, k, r, r, k,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    k, k, k, k, k, r, r, k,
    k, k, k, k, r, r, k, k,
    k, k, k, r, r, k, k, k,]
    sense.set_pixels(arrow)
    #Koden kjører tre gonger, med mellomrom på 0.75 sec, og den siste retningen blir registrert
    for i in range (10):
        #Setter variabelen acceleration til å hente informasjon frå akselerometeret, denne informasjonen kjem i listeformat
        acceleration = sense.get_accelerometer_raw()
        #Frå lista hentar vi ut x og y verdiane
        x = round(acceleration['x'], 0)
        y = round(acceleration['y'], 0)
        #z = round(acceleration['z'],)
        #For kvar iterasjon blir skjermen rotert slik at pila peiker nedover
        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)
        sleep(1)
        i+=1
    #Når programmet er ferdig å køyre må vi huske å rotere skjermen tilbake til startstilling
    sense.set_rotation(0) 
    #Returnerar x og y verdiane i siste rotasjon til loggen(slik at det er raskt å sjekke resultatet) og main(slik at vi kan skrive til csv)
    print("X og Y orienteringa er: ", x, y)
    return(x, y)
  
  
""""
    Funksjonen sitt føremål er å teste ut termometeret,
    og gi brukaren ei melding som viser temperaturen og ein liten kommentar i led-matrisa
""""   
def fun_2():
    #Hentar temperaturen frå senseHat og legg den inn i ein variabel temp
    temp = sense.get_temperature()
    #Skriv til loggen kva temperaturen er
    print("Temperaturen er: ", temp)
   
    #Brukar if-elif-else for å avgjere kva melding brukaren skal få i led-matrisa, i tillegg til temperaturen som eit tal
    if temp >= 25 : #Dersom temperaturen er over 25 grader C
      sense.show_message(str(round(temp,1)) + " Det er jaevlig varmt!", back_colour = black , text_colour= r)
    elif 10 < temp < 25: #Dersom temperaturen er mellom 10 og 25C
      sense.show_message(str(round(temp, 1)) + " Ikke så veeeelig varmt", back_colour = black , text_colour = g) 
    else: #Dersom temperaturen er under eller lik 10C
      sense.show_message(str(round(temp,1)) + " Let it snow ", back_colour= black, text_colour = b)
    
    return temp #retunera temperaturen til main(slik at vi kan skrive til cvs)
      
""""
    Denne funksjonen hentar luftfuktigheita og skriv ein setning til brukaren
""""
def fun_3():
    #henter luftfuktigheita frå sensehat
    hum = round(sense.get_humidity(),2)
    #lagar ein string(som kan skrivast til led matrisa) frå hum variabelen
    humStr = str(hum)
    
    #skriv resultatet til loggen
    print("Humidity er:", humStr)
    #skriv resultatet til led-matrisa og brukaren 
    sense.show_message("Humidity: "+humStr+"%", back_colour=[0, 0, 0], text_colour=[255,0,255])
    return hum #Returnerar humidity til main(for å kunne skrive til csv)
  
 """"
      denne funksjonen hentar ut lufttrykket og skriv ut ei melding led-matrisa til brukaren
 """"
def fun_4():
    #Hentar ut lufttrykket frå senseHat i variabelen press, og lagar ein variabel med trykket i Bar i pressSI
    press =round(sense.get_pressure(),2)
    pressSI=round(press*(10**(-3)),2)
    #Skriv resultatet direkte i loggen
    print("Pressure in mBar:",press)
    
    #Brukar if-elif-else for å avgjere kva melding som kjem opp i led-matrisa
    if press < 1:
        #printar lavt trykk til loggen
        print("Low pressure:")
        #meldinga lavt trykk & --- Bar viser dersom press < 1
        sense.show_message(
            ("Low pressure: "+str(pressSI)+" Bar"),
            text_colour=[0, 255, 0],
            back_colour=[0, 0, 0])
        sleep(1)
        sense.clear()
    elif press > 1:
        #printar normalt trykk til loggen
        print("Normal pressure:")
        #meldinga normalt trykk & --- Bar viser dersom press > 1
        sense.show_message(
            ("Normal pressure: "+str(pressSI)+" Bar"),
            text_colour=[0, 255, 0],
            back_colour=[0, 0, 0])
        sleep(0.75)
        sense.clear
    else:
        #Dersom 
        print("No reading")
    return press #Returnerar lufttrykket i den originale einina
  
  
""""
    Denne funksjonen er sjølve programmet som skal køyre
    Her brukar vi joy-sticken slik at brukaren kan velje kva for funksjon som skal køyre på ulike tidspunkt
    Når programmet er ferdig å køyre skriv det siste resultat frå alle funksjonane inn i ei csv fil
    Derfor må brukaren minst køyre alle programma ein gong
""""
def main():
    #Vi trenger csv og dato for å logge resultata
    import csv
    from datetime import datetime
    
    #Opnar ei csv fil for å appende resultatet
    fil = open("resultat", "a")
    writer = csv.writer(fil, delimiter=";") #Fila vår skal bruke semikolon for å skille informasjon
    
    #Viser at programmet er klar til å køyre, ved å sette led-matrisa til smilefjeset idle
    sense.set_pixels(idle)
    sleep(0.5)
    
    running = True #Brukar ein variabel for å kunne avslutte programmet
    while running:
        #For kvar gong det skjer ein event på joy-sticken, skal vi køyre if-elif-else treet
        for event in sense.stick.get_events():
            #Sjekkar om eventen på joy-sticken var at ein retning blei klikka inn
            if event.action == "pressed":
                #Dersom joy-sticken blir klikka opp, vil programmet køyre fun_2, hente ut temperaturen i variabelen "two", vente litt og sette på idle fjeset igjen
                if event.direction == "up":
                    two = fun_2()
                    sleep(1)
                    sense.set_pixels(idle)
                #Dersom joy-sticken blir klikka ned, vil programmet køyre ned, hente ut luftfuktigheita i variabelen "three", vente litt og sette på idle fjeset igjen
                elif event.direction == "down":
                    three = fun_3()
                    sleep(1)
                    sense.set_pixels(idle)
                #Dersom joy-sticken blir klikka venstre, vil programmet køyre fun_4, hente ut lufttrykket i variabelen "four", vente litt og sette på idle fjeset igjen
                elif event.direction == "left":
                    four = fun_4()
                    sleep(1)
                    sense.set_pixels(idle)
                #Dersom joy-sticken blir klikka høgre, vil programmet køyre fun_1, hente ut siste x, y posisjon i variabelen "one", vente litt og sette på idle fjeset igjen
                elif event.direction == "right":
                    one = fun_1()
                    sense.set_pixels(idle)
                #Den siste moglegheita er å klikke joy-sticken inn, dette vil avslutte programmet(i while løkka) og sette skjermen til blank
                else:
                    running = False
                    sense.clear()
    #Når koden er ferdig finner vi dato og tid
    x = datetime.now()
    dato = x.strftime("%d-%m-%Y")
    time = x.strftime("%H:%M:%S")
    #Appendar dato, tid, temp, x/y, fuktigheit og trykk i csv fila som ei rad
    writer.writerow([dato, time, two, one, three, four])
    sense.clear()       
    fil.close()
    #No er programmet ferdig

if __name__ == "__main__":
    main()
