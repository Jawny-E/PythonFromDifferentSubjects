# -*- coding: utf-8 -*-
"""
Dette er originalkoden til main1, denne legger vi ikkje ved
"""


from sense_hat import SenseHat
from time import sleep, time
from datetime import datetime as dt
import csv

sense = SenseHat()

#konstanter
a = -0.0065
R = 287.06
g_0 = 9.81
N = 200
path = "/home/pi/Documents" #skriv egen mappe du ønsker dataen i
path = path.rstrip("/")+"/hoydedata.csv" #formater path riktig for å få filtypen vi vil ha

#variabler
T_1 = 16 + 273.15
p_1 = 100000 #trykket målt ved høyden h_1
h_1 = 0 #Vi gjør målingene relative dersom vi ønsker ved å sette h_1 = 0

def write_to_log(write_data):
    with open(path,"a") as f:
        f.write(str(write_data) + "\n")
        
def calc_pressure_Pa():
    p = 0
    for _ in range(N):
        p += sense.pressure
        sleep(1/N)
    return p*100/N #Vi vil ha p i Pa, og multipliserer derfor med 100 etter vi deler på N

def stick_down():
    for e in sense.stick.get_events():
        if e.direction=="down":
            return 1
        
sense.show_message("Venstre: maal Hoyre: kalibrer Ned: avbryt",0.03)
running = True
while running:
    event = sense.stick.wait_for_event()
    
    if event.direction == "left":
        start = time()
        
        write_to_log("\n\n### New measurements started at: "+ dt.now().strftime("%d/%m/%Y %H:%M:%S") + " ###\n")
        
        while stick_down() != 1:
            p = calc_pressure_Pa()
            h = (T_1/a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1
            
            now = time() - start
            
            write_to_log(str(round(now,2)) + "," + str(round(p,2)) + "," + str(round(h,2)) + "," + str(round(sense.temp,1)))
            
            sense.show_message(str(int(p_1))+" Pa "+str(round(T_1))+" K ", 0.04)
            
       
    if  event.direction == "right":
        while stick_down() != 1:
            T_1 = sense.temp + 273.15
            p_1 = calc_pressure_Pa()
            sense.show_message(str(int(p_1))+" Pa "+str(round(T_1))+" K ", 0.04)
            
            
    if event.direction == "pressed":
        print("Programmet er stoppet for hand")
        sleep(2)
        break
