#SDR Signal Processing Flow Automation  
Companion module for [SatTrack](https://github.com/hazrmard/SatTrack). Used rtl-sdr
dongles to receive and decode data.  

There are two packages:  
* _AutoReceiver_: Uses `rtl-sdr` to receive data given a frequency and stores the results
in a `wav` file.  
* _AutoDecoder_: Uses a python wrapper for AMSAT's Fox Telem package to decode data packets.  

###Installation
####Prerequisites
* Python 2.7+ / 3.3+  
* Java runtime environment  
* [SOX](https://sourceforge.net/projects/sox/)  
* rtl-sdr  

`SOX` and `rtl-sdr` binaries should be in the system path.

To install:
```
> python setup.py install   # basic install, install dependencies manually 
> python setup.py install --simple-install  # install sox and rtl-sdr  
```  

Note: `--simple-install` handles path variables for `sox` and `rtl-sdr`. The system
 path still needs to be set for `java`.  
For usage instructions, see individual package `README.md` files.
