from . import os_version

modules = [["os_version", os_version.module]]


def load_modules(db):
    for name, module in modules:
        print(f'Loading module "{name}"')
        db.createmodule(name, module())
        db.execute(f"CREATE VIRTUAL TABLE {name} USING {name}()")
