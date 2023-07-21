import urllib.request
import time


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

while !connect()
    time.sleep(10)    
