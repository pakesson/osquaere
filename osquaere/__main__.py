import apsw

from osquaere.modules import load_modules
from osquaere.shell import Shell

if __name__ == "__main__":
    db = apsw.Connection(":memory:")
    load_modules(db)

    s = Shell(db=db)
    s.cmdloop()
