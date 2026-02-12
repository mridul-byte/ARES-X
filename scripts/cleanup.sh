#!/bin/bash
# ARES-X File 35: Trace Removal Script
echo "[!] ARES-X: Running secure cleanup..."
rm -rf payloads/*.exe
rm -rf payloads/*.apk
rm -rf logs/*.tmp
echo "[+] Workspace cleared of temporary artifacts."
