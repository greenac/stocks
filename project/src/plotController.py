import matplotlib.pyplot as plt
from src.quand import Quand
import json
import os.path as path

class StockPlotController:
    def __init__(self, stock_names):
        self.stock_names = stock_names
        self.stocks = {}

    def get_all_stocks(self):
        for stock_name in self.stock_names:
            file_name = 'files/quand_files/' + stock_name + '.json'
            file_path = path.join(path.dirname(path.abspath(__file__)), '..', file_name)
            try:
                with open(file_path, 'r') as stock_file:
                    stock_data = json.load(stock_file)
                    quand_list = []
                    for quand_dict in stock_data:
                        print(1)
                        quand = Quand(None, quand_dict)
                        print('quand is', str(quand))
                        quand_list.append(quand)
                    self.stocks[stock_name] = quand_list
                stock_file.close()
            except Exception as e:
                print('error opening file: ', file_name, str(e))
        return None

    def closing_prices(self, stock_name):
        print('# stocks:', len(self.stocks))
        if stock_name in set(self.stocks):
            stock_list = self.stocks[stock_name]
            prices = [stock.close for stock in stock_list]
            prices.reverse()
            return prices
        return None

    def plot_closing_prices(self):
        for stock_name in self.stock_names:
            closing_prices = self.closing_prices(stock_name)
            plt.plot([i for i in range(len(closing_prices))], closing_prices)
            plt.ylabel(stock_name + ' Price ($)')
            plt.xlabel('Number Of Days')
            plt.show()
        return None
