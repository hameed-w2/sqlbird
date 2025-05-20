# sqlbird.py

import argparse
from injector import Injector

def main():
    parser = argparse.ArgumentParser(
        description="SQLBird - Lightweight SQLi exploitation tool (Termux compatible)"
    )

    parser.add_argument('--url', required=True, help='Target URL (e.g. http://site.com/page.php?id=1)')
    parser.add_argument('--method', choices=['GET', 'POST'], default='GET', help='HTTP method to use')
    parser.add_argument('--data', help='POST data (e.g. "id=1") if method is POST')

    parser.add_argument('--test', action='store_true', help='Test if target is injectable')
    parser.add_argument('--dbs', action='store_true', help='Enumerate databases')
    parser.add_argument('--tables', action='store_true', help='Enumerate tables')
    parser.add_argument('--columns', action='store_true', help='Enumerate columns')
    parser.add_argument('--dump', action='store_true', help='Dump data from target')
    parser.add_argument('--auto', action='store_true', help='Automatically extract everything (dbs→tables→columns→dump)')

    parser.add_argument('-D', '--db', help='Database name')
    parser.add_argument('-T', '--table', help='Table name')
    parser.add_argument('-C', '--columns-list', help='Comma-separated list of columns to dump')

    parser.add_argument('--out', help='Save output to a file')

    args = parser.parse_args()

    injector = Injector(args)
    injector.run()

if __name__ == '__main__':
    main()
