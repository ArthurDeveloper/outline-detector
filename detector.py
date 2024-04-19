from PIL import Image, ImageDraw

image = Image.open('taj-mahal.png')

def color_difference(color1, color2):
    return ((color2[0] - color1[0])**2 + (color2[1] - color1[1])**2 + (color2[2] - color1[2])**2)**(1/2)

outline_pixels = []
first_color = (0, 0, 0)
for y in range(0, image.height):
    for x in range(0, image.width): 
        pixel = image.getpixel((x, y))
   
        if x == 0 and y == 0:
            first_color = pixel

        if pixel != first_color:
            past_pixel = image.getpixel((x - 1, y))

            difference = color_difference(past_pixel, pixel)
            threshold = 50

            if past_pixel == first_color or difference > threshold:
                outline_pixels.append((x, y))
                

for y in range(0, image.height):
    for x in range(0, image.width):
        if (x, y) in outline_pixels:
            image.putpixel((x, y), (255, 255, 255))
        else:
            image.putpixel((x, y), (0, 0, 0))

image.save('outline.png')
