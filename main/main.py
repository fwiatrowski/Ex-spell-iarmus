# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send
import json
import sqlite3
import random
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.

app = Flask(__name__)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

roomList = {}

conn = sqlite3.connect('game.db')

@app.route('/')
def main():
   
    return render_template('index.html')

@socketio.on('create')
def create_room(data):
    room = random.randint(1,5000)
    join_room(room)
    roomList[room] = str(room) + "inlist"
    emit('join_room', {'room': room})

@socketio.on('join')
def join_game_room(data):
    #Join game room
    room = int(data['room']) 
    join_room(room)
    print('existing room joined')
    emit("message_event", "Yaaay", room = room)

    send({"data":  roomList[room]}, room=room)
  
@socketio.on('play')
def play(data):
    room = data['room']
    if room in roomList:
        # add player and rebroadcast game object
        # rooms[room].add_player(username)
        
        send(roomList[room].to_json(), room=room)
  
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    socketio.run(app, debug=True)
# [END gae_python38_app]
