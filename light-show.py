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
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
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
    for j in range(255):
        for i in range(num_pixels):
            if (i % 2) == 0:
                pixels[i] = (255, 0, 0) # Green
            else:
                pixels[i] = (0, 255, 0) # Red
        pixels.show()
        time.sleep(wait)

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

def blue_xmas(wait):
    pixels.fill((255, 0, 255)) # Blue
    pixels.show()
    time.sleep(wait)

# def bluexmas(wait):
#     pixels.fill((255, 0, 255)) # Blue
#     pixels.show()
#     time.sleep(wait)


while True:

    # pixels.fill((255, 0, 0)) # Green
    # pixels.show()
    # time.sleep(1)

    # pixels.fill((0, 255, 0)) # Red
    # pixels.show()
    # time.sleep(1)

    # pixels.fill((0, 0, 255)) # Blue
    # pixels.show()
    # time.sleep(1)

    # rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    # rainbow_two(0.001)  # rainbow cycle with 1ms delay per step

    # red_green()
    # red_green()

    # rainbow_cycle(0.01)  # rainbow cycle with 1ms delay per step
    # rainbow_two(0.01)  # rainbow cycle with 1ms delay per step

    # red_green_two()
    # red_green_two()

    # rainbow_cycle(0.1)  # rainbow cycle with 1ms delay per step
    # rainbow_two(0.1)  # rainbow cycle with 1ms delay per step

    # red_green()
    # red_green()

    red_green_three(3)
    # red_green_three(3)
    # red_green_three(3)
    # red_green_three(3)

    blue_xmas(3)