from picovoice import Picovoice
from audiostreamlistener import AudioStreamListener
from skillmanager import SkillManager
from audioplayer import AudioPlayer
from mqttclient import MQTTClient
from utils import filehelper
import vlc


ACCESS_KEY = "/home/pi/voice-assistant-alina/access_key.txt"
KEYWORD_PATH = "/home/pi/voice-assistant-alina/wakewords/gisela_de_raspberry-pi_v2_1_0.ppn"
CONTEXT_PATH = "/home/pi/voice-assistant-alina/models/sayPhrase_de_raspberry-pi_v2_1_0.rhn"
PORCUPINE_DE_SUPPORT = "/home/pi/voice-assistant-alina/de-support/porcupine_params_de.pv"
RHINO_DE_SUPPORT = "/home/pi/voice-assistant-alina/de-support/rhino_params_de.pv"
AUDIO_MISHEARD_DIR = "/home/pi/voice-assistant-alina/audios/wakeword-callbacks/"

class Controller:

    def __init__(self):
        self.vlcPlayer = vlc.MediaPlayer()
        self.mqttClient = MQTTClient()
        self.skillManager = SkillManager(self.vlcPlayer, self.mqttClient)
        self.pv = Picovoice(
            access_key=self.__getAccessKey(ACCESS_KEY),
            keyword_path=KEYWORD_PATH,
            wake_word_callback=self.__my_wake_word_callback,
            context_path=CONTEXT_PATH,
            inference_callback=self.__inference_callback,
            porcupine_model_path=PORCUPINE_DE_SUPPORT,
            rhino_model_path=RHINO_DE_SUPPORT)

    def __my_wake_word_callback(self):
        print("Wakeword detected")
        audioPlayer = AudioPlayer("/home/pi/voice-assistant-alina/audios/button-37a.wav")
        self.skillManager.pauseCurrentSkill()
        audioPlayer.start()
        audioPlayer.join()


    def __inference_callback(self, inference):
        print(inference.is_understood)
        if inference.is_understood:
            self.skillManager.conitnueSkill()
            print(inference.intent)
            for k, v in inference.slots.items():
                print(f"{k} : {v}")
            self.skillManager.assignAndExecute(inference)
        else:
            self.skillManager.conitnueSkill()
            audioPlayer = AudioPlayer(filehelper.getRandomFileFromDir(AUDIO_MISHEARD_DIR))
            audioPlayer.start()


    def run(self):
        listener = AudioStreamListener(picovoice=self.pv, channels=1)
        listener.startListening()


    def __getAccessKey(self, filename):
        with open(filename) as f:
                return f.read()
