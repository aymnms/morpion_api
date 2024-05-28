from Status import Status

class User:
    def __init__(self, sid, uuid) -> None:
        self.sid = sid
        self.uuid = uuid
        self.status = Status(Status.WAITING)
        self.room = None

    def join_room(self, sio, room):
        self.status = Status(Status.GAME)
        self.room = room
        sio.enter_room(self.sid, self.room)
        sio.emit('message', f'{self.uuid} est rentré dans la room {self.room}', room=self.room)
    
    def leave_room(self, sio):
        if self.room:
            sio.leave_room(self.sid, self.room)
            sio.emit('message', f'{self.uuid} est sorti dans la room {self.room}', room=self.room)
        self.status = Status(Status.ENDGAME)
        self.room = None

    def is_in_game(self) -> bool:
        return self.status == Status(Status.GAME)
    
    def is_waiting(self) -> bool:
        return self.status == Status(Status.WAITING)
    
    def __str__(self) -> str:
        return f'''{self.sid}:
  {self.uuid}
  {self.status}
  {self.room}'''
    

