#import thread,threading
import subprocess
import sys
import os

localpath = os.path.dirname(__file__) + os.sep
print(localpath)
'''
usage:
1. Create an object using autoDecode(filename)
2. Call autoDecode.run to run the decoder in the background
3. Make sure that the caller program does not exit before the decoding thread finishes/aborts
'''
class autoDecode:
    '''run FoxTelem 200Hz decoder in the background thread'''
    filename = None
    def run(self):
        if not self.filename:
            print("Source .wav file name was not specified. Exiting...")
            sys.exit(1)
        subprocess.Popen(['java','-jar','autoDecode.jar',self.filename])
    def __init__(self,wavfile):
        self.filename = wavfile
