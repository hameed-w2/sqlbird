# injector.py

import requests
from modules import dbs, tables, columns, dump, autodetect
import sys

class Injector:
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.headers = {'User-Agent': 'sqlbird'}
        self.session = requests.Session()

    def log_output(self, text):
        if self.args.out:
            with open(self.args.out, 'a') as f:
                f.write(text + '\n')
        else:
            print(text)

    def run(self):
        if self.args.test:
            autodetect.test(self)
            return

        if self.args.auto:
            self.log_output("[*] Enumerating databases...")
            db_names = dbs.enumerate(self, return_list=True)

            for db_name in db_names:
                self.log_output(f"\n[*] Database: {db_name}")
                table_names = tables.enumerate(self, db_name, return_list=True)

                for table in table_names:
                    self.log_output(f"\n[**] Table: {table}")
                    col_names = columns.enumerate(self, db_name, table, return_list=True)

                    if col_names:
                        self.log_output(f"[***] Dumping columns: {', '.join(col_names)}")
                        dump.data(self, db_name, table, ",".join(col_names))
            return

        if self.args.dbs:
            dbs.enumerate(self)

        if self.args.tables and self.args.db:
            tables.enumerate(self, self.args.db)

        if self.args.columns and self.args.db and self.args.table:
            columns.enumerate(self, self.args.db, self.args.table)

        if self.args.dump and self.args.db and self.args.table and self.args.columns_list:
            dump.data(self, self.args.db, self.args.table, self.args.columns_list)
