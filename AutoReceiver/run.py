from SDR import AutoReceiver
import sys,time
def main():
            freq = '145.98M'
            file = 'test'
            # Handler for args
            for arg in range(len(sys.argv)):
                if sys.argv[arg] == '-f':
                    freq = sys.argv[arg+1]
                elif sys.argv[arg] == '-o':
                    file = sys.argv[arg+1]
            p = AutoReceiver(freq,file)
            print("started")
            time.sleep(5);
            print("about to terminate")
            time.sleep(1);
            p.terminate(True) # Set to true to delete the initial file
            print("All done! Terminating in 1 second")
            time.sleep(1)

if __name__ == '__main__': main()
