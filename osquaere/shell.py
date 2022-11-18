import apsw


class Shell(apsw.Shell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt = "osquaere> "

    def cmdloop(self):
        intro = f"""
OSQUAERE (SQLite {apsw.sqlitelibversion()}, APSW {apsw.apswversion()})
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
"""
        intro = intro.lstrip()
        super().cmdloop(intro=intro)
