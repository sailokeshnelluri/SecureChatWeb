from flask import Flask, render_template
from flask_socketio import SocketIO, send
from encryption import aes_encrypt, aes_decrypt

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

    # decrypt incoming encrypted message
    decrypted = aes_decrypt(msg)

    print("Decrypted:", decrypted)

    # encrypt again before sending
    encrypted = aes_encrypt(decrypted)

    send(encrypted, broadcast=True, include_self=False)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
