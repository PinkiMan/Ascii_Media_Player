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
Filename: main.py
"""

from utils import file_opener
import os
import sys


os.system('mode con: cols=160 lines=40')
filename = sys.argv[1]

if filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg'):
    file_opener.open_image(filename)
elif filename.endswith('gif'):
    file_opener.open_gif(filename)

input()
exit()






