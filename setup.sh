#!/bin/bash
# ARES-X File 03: Automated Termux Environment Setup

echo "------------------------------------------------"
echo "   ARES-X INDUSTRIAL INSTALLER (TERMUX MODE)    "
echo "------------------------------------------------"

# 1. Update Packages & Install Core Engines
pkg update -y && pkg upgrade -y
pkg install -y python nmap git curl wget ncurses-utils openssh

# 2. Install Metasploit (The Engine)
# This uses the official Termux-Metasploit helper
echo "[+] Installing Metasploit Framework (This may take 5-10 mins)..."
pkg install -y unstable-repo
pkg install -y metasploit

# 3. Create 35-File Structure
mkdir -p app/templates app/static core/math_layer core/network core/web core/payloads core/crypto core/exploits data/wordlists data/exploits logs scripts

# 4. Pull 4GB Industrial Data
echo "[+] Pulling Exploit-DB (~1.2GB)..."
git clone --depth 1 https://gitlab.com data/exploits

echo "[+] Pulling SecLists Wordlists (~1.8GB)..."
git clone --depth 1 https://github.com data/wordlists

# 5. Install Python Dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 6. Final Permissions
chmod +x run.py
chmod +x scripts/*.sh

echo "------------------------------------------------"
echo "   SYSTEM READY: RUN 'python run.py' TO START   "
echo "------------------------------------------------"
