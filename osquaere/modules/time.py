import datetime
import time


class TimeModule:
    schema = "CREATE TABLE x(weekday TEXT, year INTEGER, month INTEGER, day INTEGER, " \
              "hour INTEGER, minutes INTEGER, seconds INTEGER, timezone TEXT, " \
              "local_timezone TEXT, unix_time INTEGER, timestamp TEXT, " \
              "datetime TEXT, iso_8601 TEXT, win_timestamp BIGINT)"

    def Create(self, db, modulename, dbname, tablename, *args):
        return self.schema, TimeTable()
        
    def Connect(self, db, modulename, dbname, tablename, *args):
        return self.schema, TimeTable()

class TimeTable:
    def BestIndex(self, *args):
        return None
        
    def Open(self):
        return TimeCursor()
        
    def Disconnect(self):
        pass
        
    def Destroy(self):
        pass

class TimeCursor:
    def __init__(self):
        self.row = 0
        
    def Filter(self, *args):
        self.row = 0
        
    def Eof(self):
        return self.row >= 1
        
    def Next(self):
        self.row += 1
        
    def Column(self, col):
        now = datetime.datetime.now(datetime.timezone.utc)
        if col == 0:
            return now.strftime('%A')
        elif col == 1:
            return now.year
        elif col == 2:
            return now.month
        elif col == 3:
            return now.day
        elif col == 4:
            return now.hour
        elif col == 5:
            return now.minute
        elif col == 6:
            return now.second
        elif col == 7:
            return 'UTC'
        elif col == 8:
            return time.tzname[0]
        elif col == 9:
            return int(time.time())
        elif col == 10:
            return now.strftime('%Y-%m-%d %H:%M:%S')
        elif col == 11:
            return now.isoformat()
        elif col == 12:
            return now.isoformat()
        elif col == 13:
            return int(now.timestamp() * 1e7)
        else:
            raise ValueError("Invalid column number")
    
    def Rowid(self):
        return 1
        
    def Close(self):
        pass

module = TimeModule
name = "time"