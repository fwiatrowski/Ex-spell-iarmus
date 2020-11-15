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

from backend.game_objects.Game import *
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
    playerOne = data['username']

    roomList[room] = Game(playerOne)
    emit('join_room', {'room': room})

@socketio.on('join')
def join_game_room(data):
    #Join game room
    room = int(data['room']) 
    join_room(room)
    player2 = data['username']
    roomList[room].addPlayer(player2)
    roomList[room].instantiatePlayers()
    print('existing room joined')
    emit("message_event", player2 + "Joined the lobby", room = room)

    send({"data":  data['room']}, room=room)
  
@socketio.on('play')
def play(data):
    roomNumber = int(data['room'])
    room = roomList[int(data['room'])]
    playerOne = room.Player1
    playerTwo = room.Player2
    gameEnd = False
    if room.playerOneObj.Health < 0:
        emit("end_game_message", "Game over, " +playerTwo + " Won" , room = roomNumber)
        gameEnd = True
    elif room.playerTwoObj.Health < 0:
        emit("message_event", "Game over, " +playerOne + " Won" , room = roomNumber)
        gameEnd = True
    elif gameEnd == False:
        i = None
        j = None
        if data["username"] == playerOne:
            i = room.playerOneObj
            j = room.playerTwoObj
        else:
            i = room.playerTwoObj
            j = room.playerOneObj
        #Run the game spell casting etc... here
        spell = int(data['spell'])
        emit("message_event", "test", room = room)
        i.Cast(room.SpellList[spell])
        j.Hit(room.SpellList[spell])
        i.Update(i)    
        j.Update(j)
  
        print("emits below")
        emit("message_event", i.Team + "Used: " +room.SpellList[spell].Name , room = roomNumber )
        emit("game_update", {"p1Name": playerOne, "p2Name": playerTwo, "p1Health": room.playerOneObj.Health, "p2Health": room.playerTwoObj.Health,
        "p1Level": room.playerOneObj.Level, "p2Level": room.playerTwoObj.Level  } , room = roomNumber )
        emit("message_event", playerOne + "Health: " + str(room.playerOneObj.Health) , room = roomNumber )
        emit("message_event", playerTwo + "Health: " + str(room.playerTwoObj.Health) , room = roomNumber )


    

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    socketio.run(app, debug=True)
# [END gae_python38_app]
