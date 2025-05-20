# sqlbird.py
import argparse
from injector import Injector
from utils import banner

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="SQLBird - Lightweight SQLi automation tool")
    parser.add_argument("--url", help="Target URL (with injectable param)", required=True)
    parser.add_argument("--method", help="HTTP method (GET or POST)", default="GET")
    parser.add_argument("--data", help="POST data for injection")
    parser.add_argument("--cookie", help="Add custom cookie header")
    parser.add_argument("--agent", help="Set custom User-Agent")
    parser.add_argument("--tor", help="Use TOR proxy", action="store_true")

    # SQLi options
    parser.add_argument("--dbs", help="Enumerate databases", action="store_true")
    parser.add_argument("--tables", help="List tables in a DB", action="store_true")
    parser.add_argument("-D", help="Specify database name")
    parser.add_argument("--columns", help="List columns in a table", action="store_true")
    parser.add_argument("-T", help="Specify table name")
    parser.add_argument("-C", help="Specify columns to dump")
    parser.add_argument("--dump", help="Dump table data", action="store_true")

    args = parser.parse_args()

    injector = Injector(args)
    injector.run()

if __name__ == "__main__":
    main()
