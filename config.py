# ARES-X File 02: Global System Settings
import os

SECRET_KEY = os.urandom(32)
DEBUG = True

# Security & Whitelisting (Industrial Standard)
ALLOWED_TARGETS = ["127.0.0.1", "192.168.1.0/24"]
MAX_CONCURRENT_SCANS = 10

# Pathing for the 4GB Data Assets
DATA_DIR = os.path.join(os.getcwd(), 'data')
EXPLOIT_DB_PATH = os.path.join(DATA_DIR, 'exploitdb')
WORDLIST_PATH = os.path.join(DATA_DIR, 'SecLists')

# Redis Configuration for Task Queuing
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
