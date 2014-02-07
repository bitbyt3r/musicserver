from sslXMLRPC import *
from musicExceptions import *

class DJ(object):
  def __init__(self, username, password, session_id):
    self.username = username
    self.password = password
    self.session_id = session_id
    self.last_visit = get_timestamp()
    self.players = {}

  def addPlayer(self, name):
  def removePlayer(self, name):
  def startRecording(self, filename):
  def stopRecording(self):
  def recordingStatus(self):
  
class Player(object):
  def __init__(self, name):
    self.name = name
    self.playlist = []

  def add(self, songname, position):
    try:
      song = Song(songname)
      self.playlist.insert(position, song)
      return True
    except NotFound:
      return False

  def remove(self, position):
    try:
      self.playlist.pop(position)
      return True
    except IndexError:
      return False

  def get(self):
    return [x.data for x in self.playlist]

  def clear(self):
    self.playlist = []

  def play(self):
    if self.currentSong:
      if self.currentSong.length > mplayer.time_pos:
        return self.unpause()
    if not self.playlist:
      return False
    return self.next()
    
  def pause(self):
  def stop(self):
  def next(self):
  def previous(self):
  def setPosition(self, position):
  def setSpeed(self, speed):
  def status(self):

class Song(object):

class Library(object):
 def __init__(self):
 def search(self, query):

