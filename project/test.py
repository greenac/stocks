from src.quandInterface import QuandInterface
from src.plotController import StockPlotController

stocks = ['ZLTQ', 'GE', 'GOOG', 'AAPL']

spc = StockPlotController(stocks[2:3])
print('spc stocks: ', spc.stock_names)
spc.get_all_stocks()
spc.plot_closing_prices()

# qi = QuandInterface()
# for stock in stocks:
#     print('reqesting data for: ' + stock)
#     qi.request_data(stock)
# qi.write_quands_to_file()
