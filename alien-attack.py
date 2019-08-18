from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
orange = (255,165,0)

import random

one = "You are dead"
two = "Really close!"
three = "Getting closer"
four = "Alien spotted"

G = green
O = nothing
logo4 = [
    G, G, G, G, G, G, G, G,
    G, G, G, G, G, G, G, G,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

O = nothing
Y = yellow
logo3 = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    Y, Y, Y, Y, Y, Y, Y, Y, 
    Y, Y, Y, Y, Y, Y, Y, Y,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

O = nothing
X = orange
logo2 = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

O = nothing
R = red
logo1 = [
    O, O, O, O, O, O, O, O, 
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]

while True: 

  xx = random.randint(0,100)

  if (xx >= 0 and xx <= 25):
    s.show_message(str(xx) , scroll_speed=0.05, back_colour = nothing)
    time.sleep(0.75)
    s.set_pixels(logo1)
    time.sleep(0.75)
    s.show_message(str(one) , scroll_speed=0.05, back_colour = nothing)
  elif (xx >= 26 and xx <= 50):
    s.show_message(str(xx) , scroll_speed=0.05, back_colour = nothing)
    time.sleep(0.75)
    s.set_pixels(logo2)
    time.sleep(0.75)
    s.show_message(str(two) , scroll_speed=0.05, back_colour = nothing)
  elif (xx >= 51 and xx <= 75):
    s.show_message(str(xx) , scroll_speed=0.05, back_colour = nothing)
    time.sleep(0.75)
    s.set_pixels(logo3)
    time.sleep(.75)
    s.show_message(str(three) , scroll_speed=0.05, back_colour = nothing)
  elif (xx >= 76 and xx <= 100):
    s.show_message(str(xx) , scroll_speed=0.05, back_colour = nothing)
    time.sleep(0.75)
    s.set_pixels(logo4)
    time.sleep(.75)
    s.show_message(str(four) , scroll_speed=0.05, back_colour = nothing)
