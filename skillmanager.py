from phraseskill import PhraseSkill
from musicskill import MusicSkill
from lightskill import LightSkill



class SkillManager:

    def __init__(self, vlcPlayer, mqttClient):
        self.phraseSkill = PhraseSkill()
        self.musicSkill = MusicSkill(vlcPlayer, mqttClient)
        self.lightSkill = LightSkill(mqttClient)
        self.vlcPlayer = vlcPlayer

    def assignAndExecute(self, inference):

        if inference.intent == "sayPhrase":
            self.phraseSkill.execute()

        elif inference.intent == "music":
            if "type" in inference.slots:
                self.musicSkill.execute(inference.slots["var"], inference.slots["type"])
            else:
                self.musicSkill.execute(inference.slots["var"])

        elif inference.intent == "turnOnLights":
            self.lightSkill.execute(inference.slots["light"], turnOn=True)

        elif inference.intent == "turnOffLights":
            self.lightSkill.execute(inference.slots["light"], turnOff=True)


    def pauseCurrentSkill(self):
        self.musicSkill.pauseSkill()

    def conitnueSkill(self):
        self.musicSkill.continueSkill()


