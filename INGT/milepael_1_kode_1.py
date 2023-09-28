"""
Dette er koden frå deloppgåva "sjølvstendige referansepunkt"
"""


#Importer relevante modular
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
running = True #Boolsk variabel som nyttast til å stanse programmet

#Konstantar
a = -0.0065 #Temperaturgradient (kor mykje kaldare det blir per meter)
R = 287.06 #Den spesifikke gasskonstant
g_0 =9.81 #Tyngdeakselerasjonen ved havnivå
N = 200

#Variablar
T_1 = 16 + 273.15 #Temperaturen målt i h_1, i kelvin
p_1 = 10000 #Trykket målt i h_1 i Pa
h_1 = 0

#Denne funksjonen brukast til å rekne ut lufttrykket frå eit gjennomsnitt
def calc_pressure_Pa():
  p = 0
  #Vi målar trykket N-gongar og summerar alle resultata til p
  for _ in range(N):
    p += sense.pressure 
    sleep(0.001)
  #Delar på på N og får gjennomsnittet, gongar med 100 for å få svaret i Pa
  return p*100/N 

#Denne funksjonen brukast til å stanse målingar som går i loop
def stick_down():
  for e in sense.stick.get_events():
    if e.direction =="down":
      return 1
    
while running == True:
  sense.show_message("Venstre: maal - Høgre: kalibrer - Ned: Avbryt",text_colour=[255,255,255])
  event = sense.stick.wait_for_event()#Ventar på fyrste input
  
  if event.direction == "left": #Dersom joy-stick venstre, køyrer vi maal koden til joy-sticken blir tatt ned
    while stick_down() != 1:
      p = calc_pressure_Pa() #Reknar ut trykket her
      h = (T_1/a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1 #reknar ut relativ høgde frå kalibreringspunktet
      sense.show_message(str(round(h, 2)) + " m ")  #Viser den nyutrekna høgda i led-matrisa
      
  if event.direction == "right": #Dersom joy-sticken blir skubba til høgre, køyrer vi kalibrering til joy-stick ned
     while stick_down() != 1:
        T_1 = sense.temp + 273.15 #Finner referansetemperatur
        p_1 = calc_pressure_Pa() #Finner referansetrykk
        sense.show_message(str(int(p_1)) + " Pa " + str(T_1) + " K ") #Viser i led matrisa dei nye referanseverdiane

  if event.action == "pressed": #Dersom ein trykkar inn joy-sticken settast running verdien til False, og programmet vil stanse
    running = False
