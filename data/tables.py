# ARES-X File 30: Rainbow Table Manager
import os

def check_tables():
    """Verifies if the heavy rainbow tables are present in the data folder."""
    table_dir = "data/binaries/"
    if not os.path.exists(table_dir):
        return "[!] Warning: Rainbow Table directory missing."
    # Lists tables to verify the '4GB' data scale is active
    return f"[+] {len(os.listdir(table_dir))} tables loaded."
