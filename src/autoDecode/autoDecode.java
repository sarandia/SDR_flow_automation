package autoDecode;
import decoder.*;

import java.io.IOException;
import java.util.*;
import common.*;

import javax.sound.sampled.UnsupportedAudioFileException;

// Notes to get this to work with Eclipse:
// You need to add the jar via Project -> Properties -> Java Build Path -> Libraries -> Add External Jar -> Path to FoxTelem.jar
// Also, place the spacecraft directory in the project root directory


public class autoDecode {

	public static void main(String args[]){
		//FoxTelemMain.main(args);
		if (args.length == 0 ){
			System.out.println("Path to source .wav needed");
			System.exit(1);
		}
		if (args.length > 1){
			System.out.println("Too many arguments. Only 1 argument is accepted");
			System.exit(1);
		}
		String source_file = args[0];
		SourceAudio sa;
		Decoder dec;
		// All need to be "./" or defaults to root dir
		Config.homeDirectory = "./";
		Config.windowCurrentDirectory = "./";
		Config.csvCurrentDirectory = "./";
		Config.logFileDirectory = "./";
		Config.currentDir = "./";
		Config.init();
		
		Config.debugValues = false;
		Config.debugBits = false;
		Config.filterLength = 512; // Has to be 512 to work.
		Config.autoDecodeSpeed = false; // This needs to be disabled to prevent the GUI from popping up.
		try {
			sa = new SourceWav(source_file);
			dec = new Fox200bpsDecoder(sa,0);
			dec.run();
			// This seems to stall after WAV Source Exit. Manually kill it after that. 
			// Even System.exit(0) doesn't work
			
			// We can run in a thread too, but I don't think this is necessary
			//Thread thr = new Thread(dec);
			//thr.start();
	         //TThread.setUncaughtExceptionHandler(Log.uncaughtExHandler);
			//dec.run();
		} catch (UnsupportedAudioFileException | IOException e) {
			// TODO Auto-generated catch block
			System.out.println("File not found!");
			e.printStackTrace();
		}
		
	}
	
	
}
