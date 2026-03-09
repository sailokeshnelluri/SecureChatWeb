from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@socketio.on("message")
def handleMessage(msg):
    send(msg, broadcast=True, include_self=False)

@socketio.on("typing")
def typing():
    emit("typing", broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1", port=5000)