# ARES-X File 32: SQLite Interface
import sqlite3

def init_vault():
    """Initializes the local database to store industrial 'loot'."""
    conn = sqlite3.connect('data/ares_vault.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (target TEXT, vuln TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def log_finding(target, vuln, date):
    """Saves a discovered vulnerability to the persistent vault."""
    conn = sqlite3.connect('data/ares_vault.db')
    c = conn.cursor()
    c.execute("INSERT INTO results VALUES (?, ?, ?)", (target, vuln, date))
    conn.commit()
    conn.close()
