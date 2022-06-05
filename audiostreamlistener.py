import struct
import sys
import pyaudio
from picovoice import Picovoice

RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 2 
RESPEAKER_WIDTH = 2
# run getDeviceInfo.py to get index
RESPEAKER_INDEX = 1  # refer to input device id
CHUNK = 1024
ACCESS_KEY = "o0foZsUF9BFQMPWGfD3q/WoG+4EUhffHwOF0/l2BUThweEwwYBdQyQ=="
KEYWORD_PATH = "/home/pi/voice-assistant-alina/wakewords/niemand_de_raspberry-pi_v2_0_0.ppn"
CONTEXT_PATH = "/home/pi/voice-assistant-alina/models/Spruch_de_raspberry-pi_v2_0_0.rhn"
PORCUPINE_DE_SUPPORT = "/home/pi/voice-assistant-alina/de-support/porcupine_params_de.pv"
RHINO_DE_SUPPORT = "/home/pi//voice-assistant-alina/de-support/rhino_params_de.pv"


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