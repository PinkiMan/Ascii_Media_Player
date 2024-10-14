__author__ = "Pinkas Matěj"
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = "0.0.3"
__maintainer__ = "Pinkas Matěj"
__email__ = "pinkas.matej@gmail.com"
__status__ = "Prototype"
__date__ = "14/10/2024"
__created__ = "16/08/2024"

"""
Filename: main.py
"""

from utils import file_opener
import os
import sys

#os.system('resize -s 160 40')
#os.system('mode con: cols=160 lines=40')
#filename = sys.argv[1]
filename = '/Users/pinki/Desktop/Vražda_v_Orient-expresu.mp4'


if filename.endswith('png') or filename.endswith('jpg') or filename.endswith('jpeg'):
    file_opener.open_image(filename)
elif filename.endswith('gif'):
    file_opener.open_gif(filename)
elif filename.endswith('mp4'):
    file_opener.open_mkv(filename, 25*60*0)

input()
exit()






