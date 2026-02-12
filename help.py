# ARES-X File: help.py (Official Enterprise Support)
import os

def show_help():
    # Industrial Terminal Banner
    banner = r"""
    #################################################
    #   ____  ____  _____ ____        __  __        #
    #  / _  ||  _ \| ____/ ___|       \ \/ /        #
    # | |_| || |_) |  _| \___ \  ____  \  /         #
    # |  _  ||  _ <| |___ ___) ||____| /  \         #
    # |_| |_||_| \_\_____|____/       /_/\_\        #
    #                                               #
    #     [ OFFICIAL ARES-X GLOBAL SUPPORT ]        #
    #################################################
    """
    
    manual = """
    ARES-X OPERATIONAL MANUAL (FOR BEGINNERS)
    ------------------------------------------
    
    1. STARTING THE ENGINE:
       Type 'python3 run.py' and look for the server link.
       
    2. OPENING THE DASHBOARD:
       Go to your browser and enter: http://127.0.0.1:5000
       (This is your private website link to control the tool).

    3. HOW TO USE THE TOOLS:
       - NETWORK SCANNER: Enter a Target IP -> Click 'Scanner'.
       - AUTO-PWN: Matches scan results with our Global Exploit Feed.
       - WEAPONIZATION: Create Windows (.exe) or Android (.apk) test files.

    4. PUBLIC / REMOTE ACCESS:
       To share your dashboard link with others or access it away from home,
       run this in a second terminal window:
       'ssh -R 80:localhost:5000 nokey@localhost.run'

    5. DATABASE MAINTENANCE:
       Run 'bash scripts/update_db.sh' to get the latest exploit news.
       
    6. SYSTEM CLEANUP:
       Run 'bash scripts/cleanup.sh' to purge old test files and logs.
    
    [!] SYSTEM STATUS: ENTERPRISE EDITION STABLE (v1.0)
    """
    
    # Use ANSI color for industrial green look
    print("\033[92m" + banner + "\033[0m")
    print(manual)

if __name__ == "__main__":
    show_help()
