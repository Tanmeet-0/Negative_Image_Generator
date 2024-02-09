from PIL import Image


def get_negative_pixel(pixel):
    negative_pixel = [0, 0, 0]
    for i in range(3):
        segment = pixel[i]
        negative_segment = 255 - segment
        negative_pixel[i] = negative_segment
    return tuple(negative_pixel)


IMAGE_TO_BE_CONVERTED_NAME = "image.jpg"
NEGATIVE_IMAGE_NAME = "converted.png"
print("Starting")
image = Image.open(IMAGE_TO_BE_CONVERTED_NAME)
negative_image = Image.new(image.mode, image.size)
width, height = image.size
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        negative_pixel = get_negative_pixel(pixel)
        negative_image.putpixel((x, y), negative_pixel)
negative_image.save(NEGATIVE_IMAGE_NAME)
negative_image.close()
image.close()
print("Completed")
