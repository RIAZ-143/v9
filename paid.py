import os, platform

 

try:

 

    import requests

 

except:

 

    os.system('pip install requests')

 

import requests

 

bit = platform.architecture()[0]

 

if bit == '64bit':

 

    from w9s import menu3

 

    menu3()

 

elif bit == '32bit':

 

    from v9 import menu3

 

    menu3()
