# -*- coding: UTF-8 -*-
from flask import Flask, url_for, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('websock.html')

if __name__ == '__main__':
    socketio.run(app)

