import struct
import sys
import pyaudio
from picovoice import Picovoice

class AudioStreamListener:

    def __init__(self, picovoice, channels):
        self.picovoice = picovoice
        self.channels = channels


    def startListening(self):
        pa = None
        audio_stream = None

        try:
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(
                rate=self.picovoice.sample_rate,
                channels=self.channels,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.picovoice.frame_length)


            print('[Listening ...]')

            while True:
                pcm = audio_stream.read(self.picovoice.frame_length)
                pcm = struct.unpack_from("h" * self.picovoice.frame_length, pcm)

                self.picovoice.process(pcm)
                
        except KeyboardInterrupt:
            sys.stdout.write('\b' * 2)
            print('Stopping ...')
        finally:
            if audio_stream is not None:
                audio_stream.close()

            if pa is not None:
                pa.terminate()
            self.picovoice.delete()