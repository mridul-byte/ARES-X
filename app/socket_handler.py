# ARES-X File 06: Real-time Terminal Streaming
from flask_socketio import emit
import time

def init_socketio(socketio):
    @socketio.on('connect')
    def handle_connect():
        print(" [!] Industrial Console: Operator Connected.")
        emit('system_msg', {'data': 'ARES-X Console Synchronized...'})

    @socketio.on('start_module')
    def handle_module_run(json):
        module_name = json.get('module')
        target = json.get('target')
        
        # Simulated Terminal Output for the 'Industrial' look
        emit('terminal_out', {'line': f"[+] Initializing {module_name} on {target}..."})
        time.sleep(1)
        emit('terminal_out', {'line': f"[!] Loading 4GB Industrial Databases..."})
        time.sleep(1)
        emit('terminal_out', {'line': f"[*] SUCCESS: Module {module_name} is now active."})
