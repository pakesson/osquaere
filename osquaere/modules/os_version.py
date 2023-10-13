import platform

import distro

from osquaere.database import SingleRowTable


class OSVersionModule:
    def Create(self, db, modulename, dbname, tablename, *args):
        columns = [
            "name",
            "version",
            "major",
            "minor",
            "patch",
            "build",
            "platform",
            "platform_like",
            "codename",
            "arch",
        ]
        data = [
            distro.name(),
            distro.version(),
            distro.major_version(),
            distro.minor_version(),
            "",
            distro.build_number(),
            distro.id(),
            distro.like(),
            distro.codename(),
            platform.machine(),
        ]
        schema = f"CREATE TABLE os_version({', '.join(map(str, columns)) })"
        return schema, SingleRowTable(columns, data)

    Connect = Create


module = OSVersionModule
name = "os_version"