# TRENGER VARIABLER
"""""
Dette er den frivillige deloppgåva, der ein skal lage eit programm som fortel deg kva etasje du er i
Vi prøvde litt å jobbe med den, men kom ikkje fram til ein ferdig kode, derfor levera vi den originale koden med få endringar
Vi kan tenke oss å legge til bl.a legge til sjølvstendige referansepunkt, mulighet for negative etasjer, ein kalibreringsfunksjon, avbryting av programmet o.l.
""""
from sense_hat import SenseHat
import time 
#Importerar relevante modular og definera fargane vi nyttar i led-matrisa
senseHat = SenseHat()
k = [255,255, 255]
b = [0, 0, 0]

#må definere path her!
#path = /home/...

#Funksjon for å skrive resultat til fil
def write_to_log(write_data):
    with open(path, "a") as f:
        f.write(str(write_data) + "\n")   #Skriv in dataen i write_data og hoppar til ny linje

#Denne funksjonen reknar ut etasjen
def calcEtasjer():
    #Konstanter
    a = -0.0065 #Temperaturgradient
    R = 287.06 #Den spesifikke gasskonstant
    g_0 = 9.81 #Tyngdeakselerasjon ved havnivå
    
    #Variabler
    T_1 = 16 + 273.15 #Temperaturen målt i første etasje
    p_1 = 101000 #Trykket målt ved første etasje
    h_1 = 0 #Startshøyden (første etasje) er definert som 0
    h_e = 3 #høyde mellom etasjene (i meter)
    
    p = senseHat.pressure*100 #Finner trykket her
    
    h =  (T_1/a)*((p/p_1)**((-a*R)/g_0))-1)+h_1    # Hypsometrisk ligning, reknar ut høgda
    etasje = h//h_e #Reknar ut etasjen frå høgda vha nedrunding av brøk
    toppetasje = 14 #Konstant som er maks etasjer

    if etasje > toppetasje:
        etasje = toppetasje #Dersom etasjen er større enn toppetasjen, setter vi etasje til å være lik toppetasje
    
    return int(etasje) #Returnerar etasjen 

def draw(h): 
     if 0 <= h <= 14:
        sense.show_message(str(h), text_colour=k) #Dersom etasjen er mellom 0 og 14 viser led-matrisa etasjen
     else:
        sense.show_letter("k", text_colour=k) #Dersom etasjen er noko anna (under 0) viser den kjeller

        
while True:
    draw(calcEtasjer())
