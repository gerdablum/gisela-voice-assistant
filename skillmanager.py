from phraseskill import PhraseSkill
from musicskill import MusicSkill
from lightskill import LightSkill



class SkillManager:

    def __init__(self, vlcPlayer, mqttClient):
        self.phraseSkill = PhraseSkill()
        self.musicSkill = MusicSkill(vlcPlayer)
        self.lightSkill = LightSkill(mqttClient)
        self.vlcPlayer = vlcPlayer

        mqttClient.subscribe(self.musicSkill)

    def assignAndExecute(self, inference):

        if inference.intent == "sayPhrase":
            self.phraseSkill.execute()
            pass

        if inference.intent == "music":
            if "type" in inference.slots:
                self.musicSkill.execute(inference.slots["var"], inference.slots["type"])
            else:
                self.musicSkill.execute(inference.slots["var"])

        if inference.intent == "turnOnLights":
            self.lightSkill.execute(inference.slots["light"], turnOn=True)
        if inference.intent == "turnOffLights":
            self.lightSkill.execute(inference.slots["light"], turnOff=True)
        pass

    def pauseCurrentSkill(self):
        self.musicSkill.pauseSkill()
        pass

    def conitnueSkill(self):
        self.musicSkill.continueSkill()
        pass


