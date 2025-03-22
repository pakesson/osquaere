# osquaere

osquaere is a Python-based toy clone of osquery, which is a framework that exposes operating system information as SQL tables. This allows you to query your system using SQL syntax to retrieve information about your operating system.

## Current modules

* `os_version`: Exposes operating system version information (name, version, platform, architecture, etc.).
* `processes` (WiP): Provides information about running processes, with different attributes exposed depending on the platform (Windows, macOS, Linux).
* `time`: Provides current time information in various formats.

## Usage
You can run the application with:
```
python -m osquaere
```
This launches an interactive shell where you can query system information. For example:
```
$ python -m osquaere
Loading module "os_version"
Loading module "processes"
Loading module "time"
OSQUAERE (SQLite 3.49.1, APSW 3.49.1.0)
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
Connected to a transient in-memory database.
osquaere> SELECT * FROM os_version;
┌────────┬─────────┬───────┬───────┬───────┬───────┬──────────┬───────────────┬──────────┬────────┐
│  name  │ version │ major │ minor │ patch │ build │ platform │ platform_like │ codename │  arch  │
│ Ubuntu │ 22.04   │ 22    │ 04    │       │       │ ubuntu   │ debian        │ jammy    │ x86_64 │
└────────┴─────────┴───────┴───────┴───────┴───────┴──────────┴───────────────┴──────────┴────────┘
```
Press Ctrl-D (Ctrl-Z on Windows) or enter `.exit` to exit.