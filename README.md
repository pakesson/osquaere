# osquaere

Toy clone of osquery written in Python.

## Supported modules

* `os_version`

## Example
```
$ python -m osquaere
Loading module "os_version"
OSQUAERE (SQLite 3.43.1, APSW 3.43.1.1)
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
Connected to a transient in-memory database.
osquaere> SELECT * FROM os_version;
┌────────┬─────────┬───────┬───────┬───────┬───────┬──────────┬───────────────┬──────────┬────────┐
│  name  │ version │ major │ minor │ patch │ build │ platform │ platform_like │ codename │  arch  │
│ Ubuntu │ 22.04   │ 22    │ 04    │       │       │ ubuntu   │ debian        │ jammy    │ x86_64 │
└────────┴─────────┴───────┴───────┴───────┴───────┴──────────┴───────────────┴──────────┴────────┘
```
