Instructions:

Constructor: 
	     Constructor takes in two string arguments: frequency and file name

	     Frequency must be in format frequency followed by multiplier. E.G. 145.98M = 145.98 MHz

	     File name need not include an extension. The file will end up as fileName.wav

	     The constructor automatically begins execution of rtl_fm and is non-blocking, of course.

AutoReceiver.terminate

	AutoReceiver.terminate take in one boolean argument: remove

	If remove is true then the intermediate file is removed.

	Terminate terminates the rtl_fm command and then converts its output to a wav.

	Do not call terminate more than once. I didn't implement any checking in it so it doesn't check to see if the process is still running.