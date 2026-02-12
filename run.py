# ARES-X File 01: Main Entry Point
import os
from flask import Flask
from flask_socketio import SocketIO
from app.routes import main_bp
from app.socket_handler import init_socketio

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config.from_pyfile('config.py')

# Register Web Routes
app.register_blueprint(main_bp)

# Initialize Real-time Streaming
socketio = SocketIO(app, cors_allowed_origins="*")
init_socketio(socketio)

if __name__ == '__main__':
    print(" [!] ARES-X INDUSTRIAL FRAMEWORK ONLINE")
    print(" [>] Access Dashboard: http://127.0.0.1:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
