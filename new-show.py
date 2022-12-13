# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
from colorzero import Color
from time import sleep

# generate random floating point values
from random import seed
from random import random


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 450

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=.5, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

# seed random number generator
seed(1)

# Set to LED number for top of Xmas Tree. LEDs are numbered 0-24.
TOP_LED = 3


colors = [Color('cyan'), Color('yellow'), Color('purple'), Color('red'), Color('green'),
  Color('blue'), Color('magenta')] # add more if you like, see https://www.rapidtables.com/web/color/RGB_Color.html#color-table.

# main loop

while True:
    # colors
    for color in colors:
        pixels.color = color
        # colour top LED white (will flash due to loop)
        pixels[TOP_LED].color = (1, 1, 1)
        val = random()/10 # trying to make it 'sparkle'
        sleep(val)

    rainbow_cycle(0.001)

        for color in colors:
        pixels.color = color
        # colour top LED white (will flash due to loop)
        pixels[TOP_LED].color = (1, 1, 1)
        val = random()/10 # trying to make it 'sparkle'
        sleep(val)

    rainbow_cycle(0.001)

    for color in colors:
        pixels.color = color
        # colour top LED white (will flash due to loop)
        pixels[TOP_LED].color = (1, 1, 1)
        val = random()/10 # trying to make it 'sparkle'
        sleep(val)

    rainbow_cycle(0.001)

    for color in colors:
        pixels.color = color
        # colour top LED white (will flash due to loop)
        pixels[TOP_LED].color = (1, 1, 1)
        val = random()/10 # trying to make it 'sparkle'
        sleep(val)