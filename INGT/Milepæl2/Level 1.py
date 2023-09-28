#level 1
from sense_hat import SenseHat
sense = SenseHat()

k = (0, 0, 0)
g = (34, 199, 105)
b = (24, 197, 219)
v = (180, 183, 184)

Level_1 = [
v, v, v, v, v, v, v, v,
v, k, k, k, k, b, k, v,
v, v, v, v, v, v, k, v,
v, k, k, k, k, k, k, v,
v, k, v, v, v, v, v, v,
v, k, k, k, k, k, k, v,
v, v, v, g, k, k, k, v,
v, v, v, v, v, v, v, v ]

sense.set_pixels(Level_1) 

print(Level_1) 
