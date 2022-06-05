

PAYLOAD_A_ON = "AA B0 21 03 08 015E 03B6 2788 28181819081818181818181818190819081908190818181908 55"
PAYLOAD_A_OFF = "AA B0 21 03 08 015E 03B6 2792 28181819081818181818181818190819081908190819081818 55"

PAYLOAD_B_ON = "AA B0 21 03 08 0168 03AC 277E 28181819081818181818181908181819081908190818181908 55"
PAYLOAD_B_OFF = "AA B0 21 03 08 0172 03A2 2774 28181819081818181818181908181819081908190819081818 55"

TV_NAMES = ["Fernseher", "Alles"]
LIGHT_CHAIN_NAMES = ["Licht", "Alle lichter", "Alles"]

class LightSkill:

    def __init__(self, mqttClient):
        self.mqttClient = mqttClient

    def execute(self, lightType, turnOn=False, turnOff=False):
        try:
            if turnOn:
                if lightType in TV_NAMES:
                    self.mqttClient.sendMessage(PAYLOAD_A_ON)
                if lightType in LIGHT_CHAIN_NAMES:
                    self.mqttClient.sendMessage(PAYLOAD_B_ON)

            elif turnOff:
                if lightType in TV_NAMES:
                    self.mqttClient.sendMessage(PAYLOAD_A_OFF)
                if lightType in LIGHT_CHAIN_NAMES:
                    self.mqttClient.sendMessage(PAYLOAD_B_OFF)
                    
        except Exception as err:
            print(err)
