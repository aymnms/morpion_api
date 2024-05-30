from flask import Flask, request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS  # Vous devrez peut-être installer ce paquet
from Player import Player

app = Flask(__name__)
CORS(app) # Configure CORS globalement pour l'application
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*") # Permettre tous les domaines
sio = socketio.server

online_clients: dict = {}

@socketio.event
def disconnect():
    client_sid = request.sid
    if client_sid and client_sid in online_clients:
        player = online_clients[client_sid]
        if player.is_in_game():
            # donner victoire adversaire
            player.leave_room(sio)
    del online_clients[client_sid]
    print(f'[server] {client_sid} disconnected')

@socketio.event
def login(data):
    if not data:
        print('[server] ⚠️ no data has been received from client')
        return
    client_sid = request.sid
    online_clients[client_sid] = Player(client_sid, data['uuid'])
    player = online_clients[client_sid]
    print(f"[server] {player.sid} logged")
    create_room_if_possible()

def display_online_clients():
    print('[server] online clients:')
    for player in online_clients.values():
        print(player)

def create_room_if_possible():
    waiting_players = []
    for player in online_clients.values():
        if player.is_waiting:
            waiting_players.append(player.sid)
    if len(waiting_players) > 1:
        create_room(waiting_players[0], waiting_players[1])

def create_room(player1_sid, player2_sid):
    if player1_sid and player2_sid:
        room_name = player1_sid + 'xxx' + player2_sid
        online_clients[player1_sid].join_room(sio, room_name)
        online_clients[player2_sid].join_room(sio, room_name)
        # send message room pour débuter partie
        

if __name__ == '__main__':
    socketio.run(app, debug=True)
