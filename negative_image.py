from PIL import Image

def get_negative_pixel(pixel):
    negative_pixel = [0,0,0]
    for i in range(3):
        segment = pixel[i]
        negative_segment = 255-segment
        negative_pixel[i] = negative_segment
    return tuple(negative_pixel)

print("Starting")
image = Image.open("image.jpg")
negative_image = Image.new(image.mode,image.size)
width,height = image.size
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x,y))
        negative_pixel = get_negative_pixel(pixel)
        negative_image.putpixel((x,y),negative_pixel)
negative_image.save("converted.png")
negative_image.close()
image.close()
print("Completed")
