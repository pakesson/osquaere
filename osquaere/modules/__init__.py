import inspect

import apsw

from . import os_version, processes, time


modules = [os_version, processes, time]

def load_modules(db):
    for module in modules:
        print(f'Loading module "{module.name}"')
        if inspect.isclass(module.module):
            db.createmodule(module.name, module.module())
            db.execute(f"CREATE VIRTUAL TABLE {module.name} USING {module.name}()")
        else:
            apsw.ext.make_virtual_module(db, module.name, module.module)
