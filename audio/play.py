
import pyaudio
import wave
import sys
import os
import mad

CHUNK = 1024

def playmp3(filename):
	mf = mad.MadFile(filename)
	p=pyaudio.PyAudio()

	#open stream
	stream = p.open(format = 
			p.get_format_from_width(pyaudio.paInt32),
			channels=2,
			rate=mf.samplerate(),
			output=True)

	#read data
	data = mf.read()
	
	#play stream
	while data != None:
		stream.write(data)
		data = mf.read()

	stream.close()
	p.terminate()

def playwav(filename):
	wf = wave.open(filename)
	
	# instantiate PyAudio 
	p = pyaudio.PyAudio()
	stream - p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

	# read data
	data = wf.readframes(CHUNK)
	
	# play stream (3)
	while data != '':
		stream.write(data)
		data = fileHandle.readframes(CHUNK)

	# stop stream (4)
	stream.stop_stream()
	stream.close()
	
	# close PyAudio (5)
	p.terminate()


if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

name,ext = os.path.splitext(sys.argv[1])

if ext == ".mp3":
	playmp3(sys.argv[1])
elif ext == ".wav":
	playwav(sys.argv[1])


