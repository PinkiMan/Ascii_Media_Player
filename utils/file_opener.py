__author__ = "Pinkas Matěj"
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = "0.0.2"
__maintainer__ = "Pinkas Matěj"
__email__ = "pinkas.matej@gmail.com"
__status__ = "Prototype"
__date__ = "14/10/2024"
__created__ = "16/08/2024"

"""
Filename: file_opener.py
"""

import os, time, sys, cv2
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


def open_mkv(filename, skip = None):
    cam = cv2.VideoCapture(filename)

    fps = cam.get(cv2.CAP_PROP_FPS)

    if skip is not None:
        cam.set(1, skip)

    frameno = 0
    while True:
        size = os.get_terminal_size()

        start = time.time()
        ret, cv_frame = cam.read()


        if ret:
            converted = cv2.cvtColor(cv_frame, cv2.COLOR_BGR2RGB)

            pil_im = Image.fromarray(converted)
            media_to_ascii.show(pil_im, size)
            end = time.time()

            wait_time = 1/fps

            sleep = wait_time-(end-start)
            if sleep < 0:
                sleep = 0
            time.sleep(sleep)
            frameno += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()


