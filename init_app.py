from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# import socketio
# import socket
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio2 = SocketIO(app, logger=True,engineio_logger=True)


@app.route('/')
def index():
    return render_template('index.html')


def call_back(x):
    print('message was received! .. by user')


@socketio2.on('my event')
def test_message(message):
    print("my event event : ")
    print(message)
    emit('my response', {'data': message['data']})


@socketio2.on('message')
def test_message(message):
    print("message event : ")
    print(message)
    emit('message', {'data': message})


@socketio2.on('my broadcast event', namespace='/chat')
def test_message(message):
    print("my broadcast event : ")
    print(message)
    emit('my response', {'data': message['data']}, broadcast=True)

    print('emit my broadcast')


@socketio2.on('connect')
def test_connect():
    print("connect")
    emit('my response', {'data': 'Connected'})


@socketio2.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio2.run(app, debug=True)
