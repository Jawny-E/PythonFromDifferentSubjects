# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:32:29 2021

@author: Bruker
"""

#Importerar dei ulike kodebiblioteka vi treng (senseHat, avventing, tid, dato og csv)
from sense_hat import SenseHat
from time import sleep, time
from datetime import datetime as dt
import csv

sense = SenseHat()

#konstantar henta frå oppgåveteksten
a = -0.0065 #Temperaturgradient
R = 287.06 #Den spesifikke gasskonstant
g_0 = 9.81 #Tyngdeakselerasjonen ved havnivå
N = 200
path = "/home/pi/Documents" #skriv eiga mappe du ønsker dataen i
path = path.rstrip("/")+"/hoydedata.csv" #formater path riktig for å få filtypen vi ynskjer

#variabler
T_1 = 16 + 273.15 #temperatur målt ved h_1 omgjort til kelvin
p_1 = 100000 #trykket målt ved høyden h_1
h_1 = 0 #Vi gjør målingene relative dersom vi ønsker ved å sette h_1 = 0


#Denne funksjonen bruker vi for å skrive inn data i csv fila, den tar inn ein variabel(write_data) og skriv den inn
def write_to_log(write_data):
    #Brukar with open, for at fila skal opne/lukke seg automatisk kvar gong noke blir lagt til
    with open(path,"a") as f:
        #Skriver inn write_data i csv fila og hoppar til ny linje
        f.write(str(write_data) + "\n")

#Denne funksjonen gir oss lufttrykket i Pascal        
def calc_pressure_Pa():
    p = 0
    #Køyrer koden N(200) gongar, dette gjer vi for å få eit gjennomsnitt av målingar(meir nøyaktig med sensehat)
    for _ in range(N):
        p += sense.pressure #Variabelen p blir totalen av alle målingane
        sleep(1/N)
    return p*100/N #Vi vil ha p i Pa, og multipliserer derfor med 100 etter vi deler på N

#Denne funksjonen avslutter måling eller kalibrering
def stick_down():
    for e in sense.stick.get_events():
        if e.direction=="down":
            return 1
        
sense.show_message("Venstre: maal Hoyre: kalibrer Ned: avbryt",0.03)

#Det som er skrive under er det som skjer mens programmet køyrer
running = True
while running:
    event = sense.stick.wait_for_event()
    
    #Dersom ein trykker til venstre startar programmet målingane
    if event.direction == "left":
        start = time()
        
        #Når målingane startar blir tidspunktet logga i csv fila
        write_to_log("\n\n### New measurements started at: "+ dt.now().strftime("%d/%m/%Y %H:%M:%S") + " ###\n")
        #Målingane fortsett til ein tek spaken ned
        while stick_down() != 1:
            #Reknar ut trykket
            p = calc_pressure_Pa()
            #reknar ut relativ høgde, der du er no, i forhald til h_1
            h = (T_1/a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1
            now = time() - start
            #Skriver til csv-fila tid, trykk, høgde, temperatur
            write_to_log(str(round(now,2)) + "," + str(round(p,2)) + "," + str(round(h,2)) + "," + str(round(sense.temp,1)))
            #Viser i led-matrisa kva målingane her er
            sense.show_message(str(int(p_1))+" Pa "+str(round(T_1))+" K ", 0.04)
            
   #Kalibrerar temperatur og lufftrykk(i startpunktet)    
    if  event.direction == "right":
        #Fortsett å kalibrere til brukaren tar spaken ned
        while stick_down() != 1:
            T_1 = sense.temp + 273.15
            p_1 = calc_pressure_Pa()
            sense.show_message(str(int(p_1))+" Pa "+str(round(T_1))+" K ", 0.04)
            
   #Manuell avbryting av programmet når ein trykker inn joysticken      
    if event.direction == "pressed":
        print("Programmet er stoppet for hand")
        sleep(2)
        break
