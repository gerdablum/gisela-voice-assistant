from audioplayer import AudioPlayer
from utils import filehelper

AUDIO_PHRASES_DIR = "/home/pi/voice-assistant-alina/audios/phrases/"
class PhraseSkill:

    def execute(self):
        audioPlayer = AudioPlayer(filehelper.getRandomFileFromDir(AUDIO_PHRASES_DIR))
        audioPlayer.start()
    


