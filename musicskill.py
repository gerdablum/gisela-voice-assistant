import vlc
from enum import Enum
import re

MP3_STREAM_URL_HIP_HOP = "http://stream.jam.fm/rap"
MP3_STREAM_ENTSPANNUNG = "https://streams.fluxfm.de/yogasounds/mp3-128/streams.fluxfm.de/"
MP3_STREAM_ROCK = "https://d121.rndfnk.com/ard/mdr/284321/1/aac/128/stream.aac?aggregator=liveradio-de&sid=2A7DuxM9XfsxPEHeYwiFkwPZoCi&token=LTJzwzSUYvd2if7Qc0z-fNVwqYs_RfUye0QKXtDchmU&tvf=SbgW5PuD9RZkMTIxLnJuZGZuay5jb20"
MP3_STREAM_DANCE = "https://streams.fluxfm.de/klubradio/mp3-128/audio/"
MP3_STREAM_INDIE = "http://stream.laut.fm/alternative-radio"
MP3_STREAM_POP = "http://stream.jam.fm/pop"

class MusicType(Enum):
    RAP = "Rap"
    HIPHOP = "HipHop"
    ROCK = "Rock"
    RELAX = "Entspannung"
    POP = "Pop"
    INDIE = "Indie"
    DANCE = "Dance"


class MusicSkill:

    def __init__(self, player):
        
        self.player = player
        self.startCommands = ["spiele", "starte", "starten", "an"]
        self.stopCommands = ["stop", "aufhören", "stoppen", "aus"]
        self.setUrl(MP3_STREAM_URL_HIP_HOP)

        # we need this flag to distinguish if the music was just interrupted or turned off
        self.wasPlaying = False


    def setUrl(self, url):
        media = vlc.Media(url)
        if not self.player.is_playing():
            self.player.set_media(media)

    def _setUrlByMusicType(self, type):
        if type is None:
            self.setUrl(MP3_STREAM_URL_HIP_HOP)
        if type == MusicType.RAP.value or type == MusicType.HIPHOP.value:
            self.setUrl(MP3_STREAM_URL_HIP_HOP)
        elif type == MusicType.ROCK.value:
            self.setUrl(MP3_STREAM_ROCK)
        elif type == MusicType.RELAX.value:
            self.setUrl(MP3_STREAM_ENTSPANNUNG)
        elif type == MusicType.DANCE.value:
            self.setUrl(MP3_STREAM_DANCE)
        elif type == MusicType.INDIE.value:
            self.setUrl(MP3_STREAM_INDIE)
        elif type == MusicType.POP.value:
            self.setUrl(MP3_STREAM_POP)
        else:
            self.setUrl(MP3_STREAM_URL_HIP_HOP)


    def execute(self, command, musicType = None):

        if command in self.startCommands:
            self._setUrlByMusicType(musicType)
            self.player.play()
            self.wasPlaying = True
        elif command in self.stopCommands:
            self.player.stop()
            self.wasPlaying = False

    def pauseSkill(self):
        self.player.stop()

    def continueSkill(self):
        if not self.player.is_playing() and self.wasPlaying:
            self.player.play()

    
    def onMusicCommandReceived(self, payload):
        command = payload.decode("utf-8") 
        if (command == "off"):
            self.player.stop()
            self.wasPlaying = False
        if (command == "on") and not self.player.is_playing():
            self.player.play()
            self.wasPlaying = True
