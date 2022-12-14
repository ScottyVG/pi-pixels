# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
import random


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 450

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

# colors
white = (255, 255, 255)
off = (0, 0, 0)
grey = (128, 128, 128)
magenta = (255, 0, 127)
pink = (255, 0, 255)
violett = (127, 0, 255)
blue = (0, 0, 255)
light_blue = (0, 127, 255)
cyan = (0, 255, 255)
blue_green = (0, 255, 127)
green = (0, 255, 0)
yellow_green = (127, 255, 0)
yellow = (255, 255, 0)
orange = (255, 127, 0)
brown = (127, 63, 0)
orange_red = (255, 63, 0)
red_orange = (255, 127, 0)
red_pink = (255, 0, 127)
red = (255, 0, 0)

def fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)

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

def rainbow_two(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            if (i % 2) == 0:
                pixels[i] = wheel(pixel_index & 127)
            else:
                pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def green_red_run(wait):
    for i in range(num_pixels):
        if (i % 2) == 0:
            pixels[i] = (0, 255, 0) # Red
        else:
            pixels[i] = (255, 0, 0) # Green
        pixels.show()
        time.sleep(wait)

def red_green_run(wait):
    for i in range(num_pixels):
        if (i % 2) == 0:
            pixels[i] = (255, 0, 0) # Green
        else:
            pixels[i] = (0, 255, 0) # Red
        pixels.show()
        time.sleep(wait)

def green_red_wait(wait):
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(wait)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(wait)

def red_green_wait(wait):
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(wait)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(wait)


def red_green():
    # ho ho hoo
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.50)
    # ho ho hoo
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.50)
    # ho ho ho ho hoo
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.50)
    # ho ho hoo - ta ho hoo - da ho ho ho ho hoo - hoo
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.50)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.50)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.25)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(.25)
    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(.50)
    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(1)

def fill_random(wait):
    for i in range(num_pixels):
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(wait)

def fill_random_two(wait):
    for i in range(num_pixels):
        if (i % 2) == 0:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(wait)

def fill_random_three(wait):
    for i in range(num_pixels):
        if (i % 3) == 0:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(wait)

def fill_random_four(wait):
    for i in range(num_pixels):
        if (i % 4) == 0:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels.show()
        time.sleep(wait)

def fill_all_random(wait):
    pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pixels.show()
    time.sleep(wait)

def fill_random_show(wait):
    fill_random_two(wait)
    # fill(off, 0.01) # Off
    # fill_random_three(wait)
    # fill(off, 0.01) # Off
    # fill_random_four(wait)
    # fill(off, 0.01) # Off

def shooting_star(wait):
    for i in range(num_pixels):
        pixels[i] = (255, 255, 255)
        pixels.show()
        time.sleep(wait)
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
        pixels.show()
        time.sleep(wait)

# cycle
def cycle(wait, color):
    for i in range(num_pixels):
        for j in range(num_pixels):
            pixels[j] = (0, 0, 0)
        pixels[i % num_pixels] = color
        pixels.write()
        time.sleep(wait)
# # cycle
# def cycle(wait):
#     for i in range(4 * num_pixels):
#         for j in range(num_pixels):
#             pixels[j] = (0, 0, 0)
#         pixels[i % num_pixels] = (255, 255, 255)
#         pixels.write()
#         time.sleep(wait)

# bounce
def bounce(wait, color):
    for i in range(num_pixels):
        for j in range(num_pixels):
            pixels[j] = color
        if (i // num_pixels) % 2 == 0:
            pixels[i % num_pixels] = (0, 0, 0)
        else:
            pixels[num_pixels - 1 - (i % num_pixels)] = (0, 0, 0)
        pixels.write()
        time.sleep(wait)

# fade in/out
def fade_green():
    for i in range(0, 4 * 256, 8):
        for j in range(num_pixels):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            pixels[j] = (val, 0, 0)
        pixels.write()
def fade_red():
    for i in range(0, 4 * 256, 8):
        for j in range(num_pixels):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            pixels[j] = (0, val, 0)
        pixels.write()

# clear
def clear():
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.write()



def christmas():
    red_green_run(.0001)
    fill(off, .001) # Off
    fill(red, .001) # Off
    fill(off, .001) # Off
    fill(green, .001) # Off
    fill(off, .001) # Off
    fill(red, .01) # Off
    fill(off, .001) # Off
    fill(green, .01) # Off
    fill(off, .001) # Off
    fill(red, .001) # Off
    fill(off, .001) # Off
    fill(green, .001) # Off
    fill(off, .001) # Off
    fill(red, .01) # Off
    fill(off, .001) # Off
    fill(green, .01) # Off
    fill(off, .001) # Off
    fill(red, .01) # Off
    fill(off, .001) # Off
    fill(green, .01) # Off
    fill(off, .001) # Off

def red_green_show():
    red_green_wait(1)
    red_green_wait(1)
def green_red_show():
    red_green_wait(1)
    red_green_wait(1)

def blue_xmas():
    fill(blue, 5)
    fill(off, .01) # Off
    fill(white, 5)
    fill(off, .01) # Off
    fill(blue, 4)
    fill(off, .01) # Off
    fill(white, 4)
    fill(off, .01) # Off
    fill(blue, 3)
    fill(off, .01) # Off
    fill(white, 3)
    fill(off, .01) # Off
    fill(blue, 2)
    fill(off, .01) # Off
    fill(white, 2)
    fill(off, .01) # Off
    fill(blue, 1)
    fill(off, .01) # Off
    fill(white, 1)
    fill(off, .01) # Off
    fill(blue, .5)
    fill(off, .01) # Off
    fill(white, .5)
    fill(off, .01) # Off
    fill(blue, .25)
    fill(off, .01) # Off
    fill(white, .25)
    fill(off, .01) # Off
    fill(blue, .1)
    fill(off, .01) # Off
    fill(white, .1)
    fill(off, .01) # Off
    fill(blue, .01)
    fill(off, .01) # Off
    fill(white, .01)
    fill(off, .01) # Off
    fill(blue, .01)
    fill(off, .01) # Off
    fill(white, .01)
    fill(off, .01) # Off
    fill(blue, .01)
    fill(off, .01) # Off
    fill(white, .01)
    fill(off, .01) # Off
    fill(blue, .01)
    fill(off, .01) # Off
    fill(white, .01)
    fill(off, .01) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .01)
    fill(off, .001) # Off
    fill(white, .01)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .01)
    fill(off, .001) # Off
    fill(white, .01)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .001)
    fill(off, .001) # Off
    fill(white, .001)
    fill(off, .001) # Off
    fill(blue, .001)

while True:
    # cycle(.0001, white)
    # bounce(.01, red)
    # bounce(.01, green)
    # fade_red()
    # cycle(.0001, green)
    # fade_red()
    # fade_green()
    # cycle(.0001, red)
    # red_green_show()
    # christmas()
    # green_red_show()
    # christmas()
    # red_green_show()
    # fill_all_random(2)
    # fill(off, .01) # Off
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    # fill(off, .01) # Off
    # fill_all_random(2)
    # fill(off, .01) # Off
    # red_green()
    # fill_all_random(2)
    # fill(off, .01) # Off
    # fill_random_show(.001)
    # fill_all_random(2)
    # fill(off, .01) # Off
    rainbow_two(0.001)  # rainbow cycle with 1ms delay per step
    # fill_all_random(2)
    # blue_xmas()