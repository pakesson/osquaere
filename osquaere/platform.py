from enum import Enum
import platform


class Platform(Enum):
    LINUX = 1
    WINDOWS = 2
    DARWIN = 3
    UNKNOWN = 4

    @staticmethod
    def get_platform():
        sys = platform.system()
        if sys == "Linux":
            return Platform.LINUX
        elif sys == "Windows":
            return Platform.WINDOWS
        elif sys == "Darwin":
            return Platform.DARWIN
        else:
            return Platform.UNKNOWN
