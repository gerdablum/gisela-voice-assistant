# Gisela voice assistant

Gisela is a personal voice assistant. Current skills:
* say useless phrases
* play music with different genres
* turn on and off lights

## Hardware requirements
* Raspberry Pi Model 4b
* USB speaker and microphone
* optional: Sonoff RF bridge for IoT extenstions

## Software components
* python min. 3.7
* picovoice engine
* optional MQTT for IoT

## Setup
Go to console.picovoice.ai and setup an account.
In your user profile copy the access-key. Paste your access key in a file on project level and name it `access-key.txt`.

Train your wakeword (prefer to choose "Gisela") and place the training file (.ppn)
in folder `/models`. In `controller.py` rename the variable `KEYWORD_PATH` to the right filename.
Do the same with your intent training file (.rhn) and rename the `CONTEXT_PATH` variable.

Place your audio played when gisela did not understand you in `./audios/wakeword-callbacks`.

Install required dependencies `pip install -r requirements.txt`.
Start your voice assistant with `python3 picovoice-test.py`.