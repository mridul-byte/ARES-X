#!/bin/bash
# ARES-X File 03: Deployment & 4GB Data Expansion

echo "------------------------------------------------"
echo "   ARES-X INDUSTRIAL FRAMEWORK INSTALLER        "
echo "------------------------------------------------"

# 1. Create 35-File Structure
mkdir -p app/templates app/static core/math_layer core/network core/web core/payloads core/crypto core/exploits data logs scripts

# 2. Install Python Environment
pip install -r requirements.txt

# 3. Pull Massive Industrial Data (The 4GB Growth)
echo "[+] Pulling Exploit-DB (~1.2GB)..."
git clone --depth 1 https://github.com data/exploitdb

echo "[+] Pulling SecLists Wordlists (~1.8GB)..."
git clone --depth 1 https://github.com data/SecLists

echo "[+] Initializing Logs and Database..."
touch logs/audit.log
echo "INSTALLATION COMPLETE. RUN 'python3 run.py' TO START."
