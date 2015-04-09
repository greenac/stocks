from src.quandlInterface import QuandleInterface

quandle_interface = QuandleInterface()
quands = quandle_interface.request_data('ZLTQ')
for quand in quands:
    print(quand)