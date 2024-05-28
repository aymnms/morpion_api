from flask import Flask, request
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS  # Vous devrez peut-être installer ce paquet
from User import User
from Status import Status

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
        user = online_clients[client_sid]
        if user.is_in_game():
            # donner victoire adversaire
            user.leave_room(sio)
    del online_clients[client_sid]
    print(f'[server] {client_sid} disconnected')

@socketio.event
def login(data):
    if not data:
        print('[server] ⚠️ no data has been received from client')
        return
    client_sid = request.sid
    online_clients[client_sid] = User(client_sid, data['uuid'])
    user = online_clients[client_sid]
    print(f"[server] {user.sid} logged")
    create_room_if_possible()

def display_online_clients():
    print('[server] online clients:')
    for user in online_clients.values():
        print(user)

def create_room_if_possible():
    waiting_users = []
    for user in online_clients.values():
        if user.is_waiting:
            waiting_users.append(user.sid)
    if len(waiting_users) > 1:
        create_room(waiting_users[0], waiting_users[1])

def create_room(user1_sid, user2_sid):
    if user1_sid and user2_sid:
        room_name = user1_sid + 'xxx' + user2_sid
        online_clients[user1_sid].join_room(sio, room_name)
        online_clients[user2_sid].join_room(sio, room_name)
        # send message room pour débuter partie
        

if __name__ == '__main__':
    socketio.run(app, debug=True)
