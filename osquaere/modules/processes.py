import dataclasses
from dataclasses import dataclass

import apsw
import apsw.ext
import psutil

from osquaere.platform import Platform

@dataclass
class RowBase:
    pid: int
    name: str
    path: str
    cmdline: str
    state: str
    cwd: str
    root: str
    uid: int
    gid: int
    euid: int
    egid: int
    suid: int
    sgid: int
    on_disk: int
    wired_size: int
    resident_size: int
    total_size: int
    user_time: int
    system_time: int
    disk_bytes_read: int
    disk_bytes_written: int
    start_time: int
    parent: int
    pgroup: int
    threads: int
    nice: int

@dataclass
class RowWindows(RowBase):
    elevated_token: int = 0
    secure_process: int = 0
    protection_type: str = ""
    virtual_process: int = 0
    elapsed_time: int = 0
    handle_count: int = 0
    percent_processor_time: int = 0

@dataclass
class RowDarwin(RowBase):
    upid: int = 0
    uppid: int = 0
    cpu_type: int = 0
    cpu_subtype: int = 0
    translated: int = 0

@dataclass
class RowLinux(RowBase):
    cgroup_path: str = ""

Row = RowBase
platform = Platform.get_platform()
if platform == Platform.WINDOWS:
    Row = RowWindows
elif platform == Platform.DARWIN:
    Row = RowDarwin
elif platform == Platform.LINUX:
    Row = RowLinux

columns = tuple(field.name for field in dataclasses.fields(Row))

class ProcessModule:
    @staticmethod
    def module_function():
        for proc in psutil.process_iter([]): # TODO: Only iterate over necessary fields
            row = Row(
                pid = proc.info["pid"],
                name = proc.info["name"],
                path = proc.info["exe"],
                cmdline = " ".join(proc.info["cmdline"]),
                state = proc.info["status"],
                cwd = proc.info["cwd"],
                root = "", # TODO
                uid = proc.info["uids"][0],
                gid = proc.info["gids"][0],
                euid = proc.info["uids"][1],
                egid = proc.info["gids"][1],
                suid = proc.info["uids"][2],
                sgid = proc.info["gids"][2],
                on_disk = 0, # TODO
                wired_size = 0, # TODO
                resident_size = 0, # TODO
                total_size = 0, # TODO
                user_time = proc.info["cpu_times"][0],
                system_time = proc.info["cpu_times"][1],
                disk_bytes_read = 0, # TODO
                disk_bytes_written = 0, # TODO
                start_time = proc.info["create_time"],
                parent = proc.info["ppid"],
                pgroup = 0, # TODO
                threads = proc.info["num_threads"],
                nice = 0 # TODO
            )

            if platform == Platform.WINDOWS:
                row.elevated_token = 0 # TODO
                row.secure_process = 0 # TODO
                row.protection_type = "" # TODO
                row.virtual_process = 0 # TODO
                row.elapsed_time = 0 # TODO
                row.handle_count = 0 # TODO
                row.percent_processor_time = 0 # TODO
            elif platform == Platform.DARWIN:
                row.upid = 0 # TODO
                row.uppid = 0 # TODO
                row.cpu_type = 0 # TODO
                row.cpu_subtype = 0 # TODO
                row.translated = 0 # TODO
            elif platform == Platform.LINUX:
                row.cgroup_path = "" # TODO

            yield row

module = ProcessModule.module_function
module.columns = columns
module.column_access = apsw.ext.VTColumnAccess.By_Attr
name = "processes"