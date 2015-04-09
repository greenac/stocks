from src.utils import property_to_string

class QuandConstants:
    def __init__(self):
        self.name = 'name'
        self.date = 'Date'
        self.open = 'Open'
        self.high = 'High'
        self.low = 'Low'
        self.close = 'Close'
        self.volume = 'Volume'
        self.ex_dividend = 'Ex-Dividend'
        self.split_ratio = 'Split Ratio'
        self.adj_open = 'Adj. Open'
        self.adj_high = 'Adj. High'
        self.adj_low = 'Adj. Low'
        self.adj_close = 'Adj. Close'
        self.adj_volume = 'Adj. Volume'

class Quand:
    def __init__(self, name, info):
        self.constants = QuandConstants()
        self.name = name
        self.date = info[self.constants.date]
        self.open = float(info[self.constants.open])
        self.high = float(info[self.constants.high])
        self.low = float(info[self.constants.low])
        self.close = float(info[self.constants.close])
        self.volume = float(info[self.constants.volume])
        self.ex_dividend = float(info[self.constants.ex_dividend])
        self.split_ratio = float(info[self.constants.split_ratio])
        self.adj_open = float(info[self.constants.adj_open])
        self.adj_high = float(info[self.constants.adj_high])
        self.adj_low = float(info[self.constants.adj_low])
        self.adj_close = float(info[self.constants.adj_close])
        self.adj_volume = float(info[self.constants.adj_volume])

    def __str__(self):
        info_string = property_to_string(self.name, '')
        info_string = property_to_string(self.date, info_string)
        info_string = property_to_string(self.high, info_string)
        info_string = property_to_string(self.low, info_string)
        return info_string
