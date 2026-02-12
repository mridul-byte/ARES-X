# ARES-X File 33: Forensics & Action Logging
import logging

# Standard logging setup for industrial auditing
logging.basicConfig(filename='logs/audit.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def audit_log(action):
    """Logs actions to the central audit file for forensic review."""
    print(f"[AUDIT] {action}")
    logging.info(action)
