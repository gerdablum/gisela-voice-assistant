from picovoice import Picovoice
from audiostreamlistener import AudioStreamListener
from skillmanager import SkillManager
from audioplayer import AudioPlayer
from mqttclient import MQTTClient
from utils import filehelper
import vlc

def getAccesssKey(filename):
    with open(filename) as f:
        	return f.read()

ACCESS_KEY = getAccesssKey("/home/pi/voice-assistant-alina/access_key.txt")
KEYWORD_PATH = "/home/pi/voice-assistant-alina/wakewords/gisela_de_raspberry-pi_v2_1_0.ppn"
CONTEXT_PATH = "/home/pi/voice-assistant-alina/models/sayPhrase_de_raspberry-pi_v2_1_0.rhn"
PORCUPINE_DE_SUPPORT = "/home/pi/voice-assistant-alina/de-support/porcupine_params_de.pv"
RHINO_DE_SUPPORT = "/home/pi/voice-assistant-alina/de-support/rhino_params_de.pv"
AUDIO_MISHEARD_DIR = "/home/pi/voice-assistant-alina/audios/wakeword-callbacks/"

vlcPlayer = vlc.MediaPlayer()
mqttClient = MQTTClient()
skillManager = SkillManager(vlcPlayer, mqttClient)

def my_wake_word_callback():
    print("Wakeword detected")
    audioPlayer = AudioPlayer("/home/pi/voice-assistant-alina/audios/button-37a.wav")
    skillManager.pauseCurrentSkill()
    audioPlayer.start()
    audioPlayer.join()

    pass


def inference_callback(inference):
    print(inference.is_understood)
    if inference.is_understood:
        skillManager.conitnueSkill()
        print(inference.intent)
        for k, v in inference.slots.items():
            print(f"{k} : {v}")
        skillManager.assignAndExecute(inference)
    else:
        skillManager.conitnueSkill()
        audioPlayer = AudioPlayer(filehelper.getRandomFileFromDir(AUDIO_MISHEARD_DIR))
        audioPlayer.start()

pv = Picovoice(
    access_key=ACCESS_KEY,
    keyword_path=KEYWORD_PATH,
    wake_word_callback=my_wake_word_callback,
    context_path=CONTEXT_PATH,
    inference_callback=inference_callback,
    porcupine_model_path=PORCUPINE_DE_SUPPORT,
    rhino_model_path=RHINO_DE_SUPPORT)
    


def main():
    listener = AudioStreamListener(picovoice=pv, channels=1)
    listener.startListening()


if __name__ == '__main__':
    main()
