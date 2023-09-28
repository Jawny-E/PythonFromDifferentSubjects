"""
Dette er koden frå "Hvordan beregne dette i Python"
"""
from sense_hat import SenseHat

senseHat = SenseHat()

# Konstanter
a = -0.0065 # Temperaturgradient (hvor mange grader kaldere luften blir per meter)
R = 287.06  # Den spesifikke gasskonstant (for tørr luft)
g_0 = 9.81  # Tyngdeakselerasjon ved havnivå (omtrent)

# Variabler
T_1 = 16 + 273.15 # Temperaturen målt ved h_1. Lagt til 273.15 slik at man ikke glemmer
# av det oppgis i Kelvin
p_1 = # Trykket målt i Pa ved høyden h_1
h_1 = 50 # Høyden ved bakkenivå ved hovedbygget til NTNU er 45 meter. Det er 50 ved
# realfagsbygget. Vi tar 50 fordi vi sannsynligvis er litt over bakken der vi sitter.
# Sett verdien til null for å gjøre målinger relative til måleområdet.
 
while True:
    p = senseHat.pressure*100 # Lagrer trykket i Pa i stedet for hPa som en variabel
    
    h = (T_1/a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1 # Den hypsometriske ligningen
    
    senseHat.show_message(str(round(h,2))+"m",0.08) #Skriver resultatet til Sense HAT
