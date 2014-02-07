from sslXMLRPC import *

class DJ(object):
  def __init__(self, username, password, session_id):
    self.username = username
    self.password = password
    self.session_id = session_id
    self.last_visit = get_timestamp()
    self.players = {}

  def addPlayer(self, name):
  def removePlayer(self, name):
  
class Player(object):
  def __init__(self, name):
    self.name = name
  
  def add(self, songname, position):
  def remove(self, position):
  def get(self):
  def clear(self):
  def play(self):
  def pause(self):
  def stop(self):
  def next(self):
  def previous():
  def setPosition(self, position):
  def setSpeed(self, speed):
  def status(self):

class Song(object):

class Playlist(object):

class Library(object):
