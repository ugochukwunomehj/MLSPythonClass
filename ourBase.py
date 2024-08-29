my_var = 'This is a python class'

my_name = 'Withubb Ltd'


print(my_var)

class_num = 500
our_bool = False #True 
our_dict = {"name": "Withubb"}
our_lis = ["name", "phone"]
our_putle = ("name", "Withubb")


# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

def my_first_func():
    """This is our first python function, we don't have any argument in this fuction."""
    name = "I am coding python now! wow!!!"
    is_python_good = True
    if is_python_good == True:
        name = "Python is realy good!!"
        print(name)

    return name

# my_first_func()

from mutagen.mp3 import MP3
from mutagen.id3 import ID3

# audio = MP3("woto.mp3")
# print(audio.info.length)
# print(audio.info.bitrate)



# audio = ID3("ebene.mp3")
# audio['title'] = f'My Love || TrapMp3.com'
# audio.save()


import io
import requests
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error

# path to our artwork..
artwork = 'web.jpg'

# path to our audio file..
audio = EasyID3("ebene.mp3")

# adding metadata to our songfile
audio["title"] = u"Ebenezer || TrapMp3.com"
audio['artist'] = u"David Ekene"
audio['album'] = u"David Ekene @TrapMp3"

# adding artwork to our song..
audio = MP3('ebene.mp3', ID3=ID3)

# remove any existing cover pics..
audio.tags.delall('APIC')

# add new cover pics..
audio.tags.add( 
    APIC(
        encoding=3,  # 3 is for utf-8
        mime='image/jpeg',  # image/jpeg or image/png
        type=3,  # 3 is for the cover image
        desc='TrapMp3 Cover',
        data=open(artwork, 'rb').read() ))

audio.save()
