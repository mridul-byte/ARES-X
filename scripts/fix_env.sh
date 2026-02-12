#!/bin/bash
# ARES-X File: scripts/fix_env.sh
echo "[!] ARES-X: Running Environment Repair & Initialization..."

# 1. Fix Permissions
chmod +x run.py
chmod +x setup.sh
chmod +x scripts/*.sh

# 2. Verify 4GB Data Structure
mkdir -p data/exploits data/wordlists payloads logs

# 3. Force Install Critical Python Libraries
pip install --upgrade pip
pip install flask flask-socketio eventlet scapy python-nmap requests cryptography

# 4. Initialize SQLite Vault (File 32)
python3 -c "import data.db_manager as db; db.init_vault()"

echo "[+] ARES-X: System Fixed. Ready for Deployment."
