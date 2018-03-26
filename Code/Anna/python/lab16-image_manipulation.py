"""
Lab 16
Finally, some images!
"""

from PIL import Image, ImageDraw, ImageSequence
from random import randint
import colorsys
import imageio
import numpy


# Pillow uses ints for RGB values, in the range of 0-255
# 'Y' is used to represent the brightness
# To convert to greyscale, set R, G, and B to Y
# Formula for brightness: Y = 0.299*R + 0.587*G + 0.114*B

img = Image.open("images/lenna.png")    # must be in same folder
width, height = img.size                # breaking up the tuple of (512, 512)
pixels = img.load()                     # allocates storage for the image and loads the pixel data

print(img.format, img.size, img.mode)   # shows: PNG (512, 512) RGB
print(type(pixels))
print(pixels)

img.show()

# make greyscale

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299 * r + 0.587 * g + 0.114 * b

        pixels[i, j] = (int(y), int(y), int(y))

img.show()

# version 2

img2 = Image.open("images/lenna.png")    # must be in same folder
width2, height2 = img2.size                # breaking up the tuple of (512, 512)
pixels2 = img2.load()                     # allocates storage for the image and loads the pixel data

print(img2.format, img2.size, img2.mode)   # shows: PNG (512, 512) RGB
print(type(pixels2))
print(pixels2)


for i in range(width2):
    for j in range(height2):
        r, g, b = pixels2[i, j]

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        # do some math on h, s, v

        h = h * .2
        s = s * .5
        v = v * .8

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        pixels2[i, j] = r, g, b

img2.show()

# put a bird on it

run = input("Do you want to make art? y/n: ")

if run == 'y':
    img3 = Image.open("images/lenna.png")
    img4 = Image.open("images/bird.png")

    put_a_bird_on_it = Image.blend(img3, img4, 0.5)

    put_a_bird_on_it.show()

    run2 = input("Do you want to make more art? y/n: ")
    if run2 == 'y':

        # put another bird on it
        img5 = Image.open("images/lenna.png")
        img6 = Image.open("images/bird2.jpg")

        put_another_bird_on_it = Image.blend(img5, img6, 0.5)

        put_another_bird_on_it.show()
    else:
        print("OK, your loss. Let's mainLoop on.")
else:
    run2 = input("Are you sure? y/n: ")
    if run2 == 'n':

        # put another bird on it
        img5 = Image.open("images/lenna.png")
        img6 = Image.open("images/bird2.jpg")

        put_another_bird_on_it = Image.blend(img5, img6, 0.5)

        put_another_bird_on_it.show()
    else:
        print("OK, your loss. Let's mainLoop on.")


# version 3

width = 512
height = 512

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# stick man!

# the origin (0, 0) is at the top-left corner
# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((0, 0), (width, height)), fill="white")

# the head
draw.ellipse([156, 30, 356, 230], fill='yellow', outline='black')

# the body
# draw a line from x0, y0, x1, y1
draw.line((256, 230, 256, 400), fill='black', width=8)

# the legs
draw.line((256, 400, 356, 500), fill='black', width=4)
draw.line((256, 400, 156, 500), fill='black', width=4)

# the arms
draw.line((256, 300, 206, 250), fill='black', width=4)
draw.line((256, 300, 306, 250), fill='black', width=4)

img.show()


# version 4


width = 512
height = 512

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()


# now let's gif a jackalope!

images = []
img7 = Image.open("images/jackalope.jpg")
np_img = numpy.asarray(img7)
print(np_img.shape)

width, height = img7.size
pixels = img7.load()

#
for k in range(10):
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r + 13) % 256
            g = (g + 13) % 256
            b = (b + 13) % 256

            pixels[i, j] = (r, g, b)

    np_img = numpy.asarray(img7)
    images.append(np_img)

imageio.mimsave('images/jackalope.gif', images)