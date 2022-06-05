import threading
import pyaudio
import wave


class AudioPlayer(threading.Thread):

    def __init__(self, audioFilePath):
        super(AudioPlayer, self).__init__()
        self.audioFilePath = audioFilePath

    def run(self):
        wf = wave.open(self.audioFilePath, 'rb')
        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        input_device_index=1)

        # read data
        data = wf.readframes(1024)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(1024)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
