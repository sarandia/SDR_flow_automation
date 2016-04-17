import subprocess
import os

SOX_LOCALPATH = os.path.dirname(__file__) + os.sep + 'sox' + os.sep
RTL_LOCALPATH = os.path.dirname(__file__) + os.sep + 'rtl-sdr' + os.sep
os.environ['PATH'] += os.pathsep + SOX_LOCALPATH + os.pathsep + RTL_LOCALPATH

class AutoReceiver:
        def __init__(self, freq, file):
                self.freq = freq
                self.file = file
                # Certain parameters are not changable.
                self.proc = subprocess.Popen(['rtl_fm', '-M', 'fm', '-f', self.freq, '-s', '25k', self.file + '.bin'])

        def terminate(self, remove):
                self.proc.terminate()
                convProc = subprocess.Popen(['sox', '-r', '25k', '-t', 'raw', '-e', 's', '-b', '16', '-c', '1', '-V1', self.file + '.bin', self.file + '.wav']);
                # We want to wait on this one
                convProc.wait()
                if(remove):
                        remProc = subprocess.Popen(['rm', self.file + '.bin'])
