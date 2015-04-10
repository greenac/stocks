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
        self.set_name(name, info)
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

    def set_name(self, name, info):
        if self.constants.name in info:
            self.name = info[self.constants.name]
        else:
            self.name = name
        return None

    def __str__(self):
        info_string = property_to_string(self.name, '')
        info_string = property_to_string(self.date, info_string)
        info_string = property_to_string(self.high, info_string)
        info_string = property_to_string(self.low, info_string)
        return info_string

    def as_dict(self):
        return {
            self.constants.name: self.name,
            self.constants.date: self.date,
            self.constants.open: self.open,
            self.constants.high: self.high,
            self.constants.low: self.low,
            self.constants.close: self.close,
            self.constants.volume: self.volume,
            self.constants.ex_dividend: self.ex_dividend,
            self.constants.split_ratio: self.split_ratio,
            self.constants.adj_open: self.adj_open,
            self.constants.adj_high: self.adj_high,
            self.constants.adj_low: self.adj_low,
            self.constants.adj_close: self.adj_close,
            self.constants.adj_volume: self.adj_volume
        }
