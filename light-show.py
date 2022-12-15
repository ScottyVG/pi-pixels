# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 450

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER
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

def red_green_three(wait):
    for i in range(num_pixels):
        if (i % 2) == 0:
            pixels[i] = (255, 0, 0) # Green
        else:
            pixels[i] = (0, 255, 0) # Red
        pixels.show()
        time.sleep(wait)

# def red_green_three_reverse(wait):
    # for i in range(num_pixels):
    #     j = num_pixels - i
    #     if (j % 2) == 0:
    #         pixels[j] = (255, 0, 0) # Green
    #     else:
    #         pixels[j] = (0, 255, 0) # Red
    #     pixels.show()
    #     time.sleep(wait)

def red_green_two():

    pixels.fill((255, 0, 0)) # Green
    pixels.show()
    time.sleep(2)

    pixels.fill((0, 255, 0)) # Red
    pixels.show()
    time.sleep(2)

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

def fill(color, wait):
    pixels.fill(color)
    pixels.show()
    time.sleep(wait)


while True:
    fill(white, 1)
    fill(off, .1)
    fill(grey, 1)
    fill(off, .1)
    fill(magenta, 1)
    fill(off, .1)
    fill(pink, 1)
    fill(off, .1)
    fill(violett, 1)
    fill(off, .1)
    fill(blue, 1)
    fill(off, .1)
    fill(light_blue, 1)
    fill(off, .1)
    fill(cyan, 1)
    fill(off, .1)
    fill(blue_green, 1)
    fill(off, .1)
    fill(green, 1)
    fill(off, .1)
    fill(yellow_green, 1)
    fill(off, .1)
    fill(yellow, 1)
    fill(off, .1)
    fill(orange, 1)
    fill(off, .1)
    fill(brown, 1)
    fill(off, .1)
    fill(orange_red, 1)
    fill(off, .1)
    fill(red_orange, 1)
    fill(off, .1)
    fill(red_pink, 1)
    fill(off, .1)
    fill(red, 1)
    fill(off, .1)

    fill(white, .5)
    fill(off, .1)
    fill(grey, .5)
    fill(off, .1)
    fill(magenta, .5)
    fill(off, .1)
    fill(pink, .5)
    fill(off, .1)
    fill(violett, .5)
    fill(off, .1)
    fill(blue, .5)
    fill(off, .1)
    fill(light_blue, .5)
    fill(off, .1)
    fill(cyan, .5)
    fill(off, .1)
    fill(blue_green, .5)
    fill(off, .1)
    fill(green, .5)
    fill(off, .1)
    fill(yellow_green, .5)
    fill(off, .1)
    fill(yellow, .5)
    fill(off, .1)
    fill(orange, .5)
    fill(off, .1)
    fill(brown, .5)
    fill(off, .1)
    fill(orange_red, .5)
    fill(off, .1)
    fill(red_orange, .5)
    fill(off, .1)
    fill(red_pink, .5)
    fill(off, .1)
    fill(red, .5)
    fill(off, .1)

    fill(white, .25)
    fill(off, .1)
    fill(grey, .25)
    fill(off, .1)
    fill(magenta, .25)
    fill(off, .1)
    fill(pink, .25)
    fill(off, .1)
    fill(violett, .25)
    fill(off, .1)
    fill(blue, .25)
    fill(off, .1)
    fill(light_blue, .25)
    fill(off, .1)
    fill(cyan, .25)
    fill(off, .1)
    fill(blue_green, .25)
    fill(off, .1)
    fill(green, .25)
    fill(off, .1)
    fill(yellow_green, .25)
    fill(off, .1)
    fill(yellow, .25)
    fill(off, .1)
    fill(orange, .25)
    fill(off, .1)
    fill(brown, .25)
    fill(off, .1)
    fill(orange_red, .25)
    fill(off, .1)
    fill(red_orange, .25)
    fill(off, .1)
    fill(red_pink, .25)
    fill(off, .1)
    fill(red, .25)
    fill(off, .1)

    fill(white, .1)
    fill(off, .01)
    fill(grey, .1)
    fill(off, .01)
    fill(magenta, .1)
    fill(off, .01)
    fill(pink, .1)
    fill(off, .01)
    fill(violett, .1)
    fill(off, .01)
    fill(blue, .1)
    fill(off, .01)
    fill(light_blue, .1)
    fill(off, .01)
    fill(cyan, .1)
    fill(off, .01)
    fill(blue_green, .1)
    fill(off, .01)
    fill(green, .1)
    fill(off, .01)
    fill(yellow_green, .1)
    fill(off, .01)
    fill(yellow, .1)
    fill(off, .01)
    fill(orange, .1)
    fill(off, .01)
    fill(brown, .1)
    fill(off, .01)
    fill(orange_red, .1)
    fill(off, .01)
    fill(red_orange, .1)
    fill(off, .01)
    fill(red_pink, .1)
    fill(off, .01)
    fill(red, .1)
    fill(off, .01)

    red_green_three(.0001)
    fill(off, .0001) # Off

    fill(green, 3) # Green
    fill(off, 1) # Off
    fill(red, 3) # Red
    fill(off, 1) # Off

    fill(green, 2) # Green
    fill(off, .5) # Off
    fill(red, 2) # Red
    fill(off, .5) # Off

    fill(green, 1) # Green
    fill(off, .25) # Off
    fill(red, 1) # Red
    fill(off, .25) # Off

    fill(green, .5) # Green
    fill(off, .125) # Off
    fill(red, .5) # Red
    fill(off, .125) # Off

    fill(green, .5) # Green
    fill(off, .125) # Off
    fill(red, .5) # Red
    fill(off, .125) # Off

    fill(green, .5) # Green
    fill(off, .125) # Off
    fill(red, .5) # Red
    fill(off, .125) # Off

    fill(green, .5) # Green
    fill(off, .125) # Off
    fill(red, .5) # Red
    fill(off, .125) # Off

    fill(green, .5) # Green
    fill(off, .125) # Off
    fill(red, .5) # Red
    fill(off, .125) # Off

    red_green_three(.001)
    fill(off, .01) # Off
    red_green_three(.001)
    fill(off, .01) # Off
    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

    red_green()
    rainbow_cycle(0.01)  # rainbow cycle with 1ms delay per step
    red_green_two()


    red_green_two()
    rainbow_two(0.01)  # rainbow cycle with 1ms delay per step
    red_green()

    rainbow_cycle(0.1)  # rainbow cycle with 1ms delay per step
    rainbow_two(0.1)  # rainbow cycle with 1ms delay per step

    red_green()
    rainbow_two(0.001)  # rainbow cycle with 1ms delay per step
    red_green()

    fill(blue, 15) # Blue
    fill(off, 2) # Off