import os, platform

 

try:

 

    import requests

 

except:

 

    os.system('pip install requests')

 

import requests

 

bit = platform.architecture()[0]

 

if bit == '64bit':

 

    from v9s import menu3

 

    menu3()

 

elif bit == '32bit':

 

    from v9-1 import menu3

 

    menu3()
