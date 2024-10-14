__author__ = "Pinkas Matěj"
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Pinkas Matěj"
__email__ = "pinkas.matej@gmail.com"
__status__ = "Prototype"
__date__ = "14/10/2024"
__created__ = "14/10/2024"

"""
Filename: ig_to_img.py.py
"""

from instaloader import Instaloader, Profile


username = ''

L = Instaloader()
L.save_metadata = False
L.download_geotags = False
L.download_comments = False

PROFILE = username
profile = Profile.from_username(L.context, PROFILE)

if (profile.is_private):
    print("User " + username + " is private")

def downloadProfilePic(L, username):
    PROFILE = username
    profile = Profile.from_username(L.context, PROFILE)
    L.download_profilepic(profile)
    print("Profile picture downloaded")

downloadProfilePic(L,username)