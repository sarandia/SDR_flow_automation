#AutoReceiver Instructions:

Constructor:
	Constructor takes in two string arguments: frequency and file name

	Frequency must be in format frequency followed by multiplier. E.G. 145.98M = 145.98 MHz

	File name need not include an extension. The file will end up as fileName.wav

	The constructor automatically begins execution of rtl_fm and is non-blocking, of course.

AutoReceiver.terminate:

	AutoReceiver.terminate take in one boolean argument: remove

	If remove is true then the intermediate file is removed.

	Terminate terminates the rtl_fm command and then converts its output to a wav.

	Terminate *is* blocking, but the conversion process shouldn't take long.

	Do not call terminate more than once. It doesn't check to see if the process is still running.

See run.py for an example.