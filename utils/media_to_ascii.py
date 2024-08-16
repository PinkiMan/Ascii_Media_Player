__author__ = "Pinkas Matěj"
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Pinkas Matěj"
__email__ = "pinkas.matej@gmail.com"
__status__ = "Prototype"
__date__ = "16/08/2024"
__created__ = "16/08/2024"

"""
Filename: media_to_ascii.py
"""

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", ' ']
ASCII_CHARS = ASCII_CHARS[::-1]


def calc_resize(image, terminal_size):
    width, height = image.size
    terminal_width, terminal_height = terminal_size
    terminal_width -= 1
    terminal_height -= 1

    image_ratio = height / width / 2

    if int(terminal_width * image_ratio) <= terminal_height:
        return terminal_width, int(terminal_width * image_ratio)
    elif int(terminal_height / image_ratio) <= terminal_width:
        return int(terminal_height / image_ratio), terminal_height


def draw_border(ascii_image, width, height):
    ascii_image = list(ascii_image)
    for y in range(height):
        for x in range(width):
            if y == 0 or y == height-1:
                ascii_image[y*(width+1)+x] = '-'
            elif x == 0 or x == width-1:
                ascii_image[y*(width+1)+x] = '|'
    return ''.join(ascii_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 23] for pixel in pixels])
    return (characters)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    return (resized_image)


def show(image, size=(317,86)):
    width, height = calc_resize(image, size)

    new_image_data = pixels_to_ascii(grayify(resize_image(image, width, height)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + width)] for index in range(0, pixel_count, width)])

    ascii_image = draw_border(ascii_image, width, height)

    print(ascii_image)

    return height



