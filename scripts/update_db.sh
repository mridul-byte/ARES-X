#!/bin/bash
# ARES-X File 34: Data Syncing Script
echo "[!] Updating 4GB Industrial Repositories..."
cd data/exploits && git pull
cd ../wordlists && git pull
echo "[+] Repositories synchronized to latest version."
