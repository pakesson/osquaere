# osquaere

Toy clone of osquery written in Python.

Example:
```
$ python -m osquaere
Loading module "os_version"
OSQUAERE
SQLite version 3.39.4 (APSW 3.39.4.0)
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
osquaere> SELECT * FROM os_version;
Arch Linux||||||arch|||x86_64
```
