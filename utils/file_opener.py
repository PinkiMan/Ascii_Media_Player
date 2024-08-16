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
Filename: file_opener.py
"""

import os, time, sys
from PIL import Image


from utils import media_to_ascii



def open_image(filename):
    image = Image.open(filename)

    os_size = os.get_terminal_size()
    last_size = [0, 0]

    while True:
        os_size = os.get_terminal_size()

        size = [int(os_size[0]), int(os_size[1])]
        if last_size != size:
            last_size = size
            height = media_to_ascii.show(image, size)


def open_gif(filename):
    SIZE = 40
    while True:
        with Image.open(filename) as image:
            for i in range(image.n_frames):
                os_size = os.get_terminal_size()
                size = [int(os_size[0]), int(os_size[1])]

                image.seek(i)
                height = media_to_ascii.show(image, size)
                time.sleep(0.05)



