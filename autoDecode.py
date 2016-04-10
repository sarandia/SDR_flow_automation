import thread,threading
from subprocess import call
import os
'''
usage:
1. Create an object using autoDecode(filename)
2. Call autoDecode.run to run the decoder in the background
3. Make sure that the caller program does not exit before the decoding thread finishes/aborts
'''
class autoDecode:
    '''run FoxTelem 200Hz decoder in the background thread'''
    filename = ""
    def run(self):
        def run_java_decoder():
            command = "java -jar autoDecode.jar"+" "+self.filename
            os.system(command)
            thread.interrupt_main()
        t = threading.Thread(target=run_java_decoder)
        t.daemon = True
        t.start()
    def __init__(self,wavfile):
        self.filename = wavfile
