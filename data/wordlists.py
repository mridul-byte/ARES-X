# ARES-X File 31: Massive Dictionary Handler
import os

def get_list(category):
    """Accesses the 4GB-scale wordlists for industrial brute-forcing."""
    # These paths link to the folders created by your setup.sh
    base = "data/wordlists/"
    paths = {
        "passwords": f"{base}Passwords/Common-Credentials/10-million-combined-list.txt",
        "web": f"{base}Discovery/Web-Content/common.txt"
    }
    return paths.get(category, "Path not found.")
