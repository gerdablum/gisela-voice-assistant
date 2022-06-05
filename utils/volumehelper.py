import alsaaudio
import subprocess

NORMAL_VOLUME = None

class VolumeHelper():

     def __init__(self):
          self.normalVolume = None

     def turnDownVolume(self):
          mixer = alsaaudio.Mixer()
          self.normalVolume = mixer.getvolume()
          subprocess.call(["amixer",  "-D", "pulse", "sset", "Master", "10%"])

     def turnUpVolume(self):
          subprocess.call(["amixer", "-D", "pulse", "sset", "Master",'{}%'.format(self.normalVolume[0]) ])
