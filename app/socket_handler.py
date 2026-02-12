# ARES-X File 06: Real-time Terminal Streaming & Command Bridge
from flask_socketio import emit
import subprocess
import time

def init_socketio(socketio):
    @socketio.on('connect')
    def handle_connect():
        print(" [!] Industrial Console: Operator Connected.")
        emit('terminal_out', {'line': '>>> ARES-X SYSTEM SYNCHRONIZED...'})

    @socketio.on('start_module')
    def handle_module_run(json):
        module_name = json.get('module')
        target = json.get('target')
        
        # 1. First, send a 'Loading' message to the web UI
        emit('terminal_out', {'line': f"[!] Accessing 4GB Industrial Database for {module_name}..."})
        
        # 2. Define the command based on the button clicked
        if module_name == "Scanner":
            command = f"nmap -A -T4 {target}"
        elif module_name == "SearchSploit":
            command = f"searchsploit {target}"
        else:
            command = f"echo 'Module {module_name} selected for {target}'"

        # 3. Call the Bridge function to stream live output
        stream_command_to_web(command, socketio)

def stream_command_to_web(command, socketio):
    """The 'Bridge' that links Terminal output to your Web Dashboard."""
    # This runs the command (Nmap, Metasploit, etc.) in the background
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
    
    # This loop catches every single line the tool prints
    for line in iter(process.stdout.readline, ""):
        # This sends it LIVE to your screen
        socketio.emit('terminal_out', {'line': line.strip()})
        # This keeps a copy in your Termux window too
        print(line.strip()) 
    
    process.stdout.close()
    process.wait()
    socketio.emit('terminal_out', {'line': '[+] EXECUTION COMPLETE.'})
