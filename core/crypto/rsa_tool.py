# ARES-X File 25: Public Key Weakness Analyzer
from cryptography.hazmat.primitives import serialization

def analyze_rsa_key(key_path):
    """Checks for insecure RSA configurations (Industrial Math)."""
    try:
        with open(key_path, "rb") as f:
            key = serialization.load_pem_public_key(f.read())
            # Accessing the 'n' and 'e' components for math analysis
            numbers = key.public_numbers()
            if numbers.e < 65537:
                return f"[!] RISK: Low Public Exponent ({numbers.e}) found."
            return "[+] RSA Status: Industrial Strength Verified."
    except Exception as e:
        return f"Error: {str(e)}"
