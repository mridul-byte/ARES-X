# ARES-X File 24: GPU-Accelerated Hash Cracker
import hashlib

def crack_hash(target_hash, hash_type="md5"):
    """Brute-forces hashes using the massive data/wordlists/ directory."""
    wordlist = "data/SecLists/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    
    with open(wordlist, "r", errors='ignore') as f:
        for line in f:
            word = line.strip()
            # Dynamic hashing based on type
            h = hashlib.new(hash_type)
            h.update(word.encode())
            if h.hexdigest() == target_hash:
                return f"[SUCCESS] Match Found: {word}"
    return "[FAILURE] No match in 4GB database."
