def show_splash():
    # This is the "letter-based" image for the terminal
    logo = """
    █████╗ ██████╗ ███████╗███████╗      ██╗  ██╗
    ██╔══██╗██╔══██╗██╔════╝██╔════╝      ╚██╗██╔╝
    ███████║██████╔╝█████╗  ███████╗█████╗ ╚███╔╝ 
    ██╔══██║██╔══██╗██╔══╝  ╚════██║╚════╝ ██╔██╗ 
    ██║  ██║██║  ██║███████╗███████║      ██╔╝ ██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝      ╚═╝  ╚═╝
    [ INDUSTRIAL RED-TEAM ORCHESTRATION SYSTEM ]
    ______________________________________________
    VERSION : 1.0.4-STABLE (ENTERPRISE EDITION)
    CORES   : 35 ACTIVE MODULES
    DATABASE: GLOBAL VULNERABILITY FEED SYNCHRONIZED
    STATUS  : ENCRYPTION TUNNEL ESTABLISHED (AES-256)
    ______________________________________________
    """
    print("\033[92m" + logo + "\033[0m") # Prints in Industrial Green
