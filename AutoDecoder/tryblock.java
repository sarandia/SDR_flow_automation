			sa = new SourceWav(n);
			dec = new Fox200bpsDecoder(sa,0);
			//dec.run();
			
			//System.out.println("test");
			//dec.stopProcessing();
			// This seems to stall after WAV Source Exit. Manually kill it after that. 
			// Even System.exit(0) doesn't work
			
			// We can run in a thread too, but I don't think this is necessary
			Thread thr = new Thread(dec);
			thr.start();
			
			// Wait until source audio is done. Either check if done or check percent progress.
						
			//while(((SourceWav) sa).getPercentProgress() < 100){
			while(!sa.isDone()){	
				// System.out.print("\rProgress: " + ((SourceWav) sa).getPercentProgress() + "%");
				// That ^ does not work on Windows for whatever reason.
				try {
					
					Thread.sleep(5L);
				} 
				catch (InterruptedException e) {
				}
			}
			// Stop processing once it's done. This caused decoder to exit the processing loop.
			dec.stopProcessing();
			// Wait for decoder to finish.
			thr.join();
			System.exit(0); // I don't know why this is necessary, but apparently it is?
