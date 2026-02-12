# ARES-X File 26: Multi-layer Decoder
import base64

def deep_decode(data, layers=5):
    """Peels back multiple layers of Base64/Hex encoding recursively."""
    current = data
    for i in range(layers):
        try:
            # Attempt to decode the current layer
            current = base64.b64decode(current).decode()
            print(f"[*] ARES-X: Layer {i+1} Stripped.")
        except:
            break 
    return current
