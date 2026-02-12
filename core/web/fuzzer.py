# ARES-X File 18: Directory & API Brute-forcer
import requests
import os

def brute_force_dirs(base_url):
    """Uses industrial wordlists to find hidden server paths."""
    wordlist = "data/SecLists/Discovery/Web-Content/common.txt"
    if not os.path.exists(wordlist):
        return "Error: 4GB Wordlist not found. Run setup.sh."

    found_dirs = []
    with open(wordlist, "r") as f:
        for line in f:
            dir_name = line.strip()
            url = f"{base_url}/{dir_name}"
            resp = requests.get(url)
            if resp.status_code == 200:
                print(f"[+] Found: {url}")
                found_dirs.append(url)
    return found_dirs
