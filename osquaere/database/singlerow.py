class SingleRowCursor:
    def __init__(self, table):
        self.table = table

    def Filter(self, *args):
        self.pos = 0

    def Eof(self):
        return self.pos > 0

    def Rowid(self):
        return 0

    def Column(self, col):
        return self.table.data[col]

    def Next(self):
        self.pos += 1

    def Close(self):
        pass


class SingleRowTable:
    def __init__(self, columns, data):
        self.columns = columns
        self.data = data

    def BestIndex(self, *args):
        return None

    def Open(self):
        return SingleRowCursor(self)

    def Disconnect(self):
        pass

    Destroy = Disconnect
