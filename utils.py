# utils.py
def banner():
    print("SQLBird - Lightweight SQL Injection Tool (for Termux)")
    print("For educational and authorized testing only.\n")

def build_headers(agent=None, cookie=None):
    headers = {}
    if agent:
        headers['User-Agent'] = agent
    if cookie:
        headers['Cookie'] = cookie
    return headers
