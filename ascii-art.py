import os
from PIL import Image

# ascii-characters
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize the image
def resize_image(image, new_width):
    width, height = image.size
    aspect_ratio = height/ width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert pixels to ascii_characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(chars)

def run(new_width):
    # get filename
    filename = input("Filename: ")
    # get absolute-path for file
    path = os.path.abspath(filename)

    try:
        image = Image.open(path).convert('L')
    except:
        print(path, " invalid path")
        return

    # converting pixels to ascii-chars
    ascii_data = pixels_to_ascii(resize_image(image, new_width))

    # format image
    pixel_count = len(ascii_data)
    ascii_img = "\n".join([ascii_data[i : (i+new_width)] for i in range(0, pixel_count, new_width)])

    print(ascii_img)

# run
run(100)