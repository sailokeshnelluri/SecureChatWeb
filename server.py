from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)

# allow connections from any device/browser
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

# message event
@socketio.on("message")
def handleMessage(msg):
    print("Message:", msg)

    # broadcast message to all users except sender
    send(msg, broadcast=True, include_self=False)

# typing indicator
@socketio.on("typing")
def typing():
    emit("typing", broadcast=True, include_self=False)

# run server
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
