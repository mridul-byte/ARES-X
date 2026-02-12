# ARES-X File 19: Security Header Auditor
import requests

def audit_headers(url):
    """Analyzes the HTTP headers for security gaps."""
    response = requests.get(url)
    headers = response.headers
    security_headers = ['Content-Security-Policy', 'X-Frame-Options', 'X-Content-Type-Options']
    
    report = {}
    for sh in security_headers:
        report[sh] = "PRESENT" if sh in headers else "MISSING (Risk)"
        
    return report
