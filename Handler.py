import os
import hmac
import uuid
from hashlib import sha256
from xmlrpc.server import *
from sslXMLRPC import *
import music

class AudioHandler:
  def __init__(self, options):
    self.sessions = {}
    self.session_key = os.urandom(32)
    self.players = {}
    self.recorders = {}
    self.users = options['users']
    self.library = music.Library()
        
  def _clear_expired_sessions(self):
    for i in list(self.sessions.keys()):
      if is_timestamp_expired(self.sessions[i].last_visit):
        try:
          del self.sessions[i]
        except KeyError:
          pass


  @require_login
  def search(self, sid, query):
    return self.library.search(query)

  @require_login
  def startRecording(self, sid, filename):
    return self.sessions[sid].startRecording(filename)

  @require_login
  def stopRecording(self, sid):
    return self.sessions[sid].stopRecording()

  @require_login
  def recordingStatus(self, sid):
    return self.sessions[sid].recordingStatus()

  @require_login
  def player_add_song(self, sid, songname, position, player):
    return self.sessions[sid].players[player].add(songname, position)

  @require_login
  def player_remove_song(self, sid, position, player):
    return self.sessions[sid].players[player].remove(position)

  @require_login
  def player_get_contents(self, sid, player):
    return self.sessions[sid].players[player].get()

  @require_login
  def player_clear_list(self, sid, player):
    return self.sessions[sid].players[player].clear()

  @require_login
  def player_clear_all(self, sid):
    for i in self.sessions[sid].players:
      self.sessions[sid].players[i].clear()
    return True

  @require_login
  def player_get_lists(self, sid):
    return self.sessions[sid].players.keys()

  @require_login
  def player_add_list(self, sid, name):
    return self.sessions[sid].addList(name)

  @require_login
  def player_remove_list(self, sid, name):
    return self.sessions[sid].removeList(name)

  @require_login
  def player_play(self, sid, name):
    return self.sessions[sid].players[name].play()

  @require_login
  def player_pause(self, sid, name):
    return self.sessions[sid].players[name].pause()

  @require_login
  def player_stop(self, sid, name):
    return self.sessions[sid].players[name].stop()

  @require_login
  def player_next(self, sid, name):
    return self.sessions[sid].players[name].next()

  @require_login
  def player_previous(self, sid, name):
    return self.sessions[sid].players[name].previous()

  @require_login
  def player_set_position(self, sid, name, position):
    return self.sessions[sid].players[name].setPosition(position)

  @require_login
  def player_set_speed(self, sid, name, speed):
    return self.sessions[sid].players[name].setSpeed(speed)

  @require_login
  def player_status(self, sid, name):
    return self.sessions[sid].players[name].status()

  @require_login
  def logout(self, sid):
    self.clients[sid].batch.clients.remove(self.clients[sid])
    del self.sessions[sid]
    del self.clients[sid]

  def login(self, username, password):
    if username in self.users:
      if self.users[username] == password:
        # generate session id and save it
        session_id = hmac.new(self.session_key, (username + str(uuid.uuid4())).encode('UTF-8'), sha256).hexdigest()
        self.sessions[session_id] = music.DJ(username=username, password=password, session_id=session_id)
        return session_id
    raise Fault("unknown username or password", "Please check your username and password")
