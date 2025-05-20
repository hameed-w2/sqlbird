import requests
from modules import dbs, tables, columns, dump, autodetect

class Injector:
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.headers = {'User-Agent': 'sqlbird'}
        self.session = requests.Session()

    def run(self):
        if self.args.test:
            autodetect.test(self)
            return

        if self.args.dbs:
            dbs.enumerate(self)

        if self.args.tables and self.args.db:
            tables.enumerate(self, self.args.db)

        if self.args.columns and self.args.db and self.args.table:
            columns.enumerate(self, self.args.db, self.args.table)

        if self.args.dump and self.args.db and self.args.table and self.args.columns_list:
            dump.data(self, self.args.db, self.args.table, self.args.columns_list)
