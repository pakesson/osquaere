import apsw
import apsw.bestpractice

from osquaere.modules import load_modules
from osquaere.shell import Shell


if __name__ == "__main__":
    apsw.bestpractice.apply(apsw.bestpractice.recommended)

    db = apsw.Connection(":memory:")
    load_modules(db)

    s = Shell(db=db)
    s.cmdloop()
