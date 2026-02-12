# ARES-X File 13: Industrial Traffic Analyzer
from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    """Processes every intercepted packet in real-time."""
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if packet.haslayer(TCP):
            print(f"[+] TRAFFIC: {ip_src} -> {ip_dst} | Port: {packet[TCP].dport}")

def start_sniffing(interface="eth0", count=10):
    """Activates the industrial sniffer drone."""
    print(f"[*] ARES-X: Sniffing on {interface}...")
    sniff(iface=interface, prn=packet_callback, count=count)
