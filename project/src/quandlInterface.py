import urllib.request as request
from src.quand import Quand

class QuandleInterface:
    def __init__(self):
        self._api_key = 'SDnxkRiZzVHTFrVgWRR4'

    def _url(self, stock_name):
        return 'https://www.quandl.com/api/v1/datasets/WIKI/' \
                     + stock_name + '.csv?auth_token=' + self._api_key

    def _make_request(self, stock_name):
        # TODO -- add error handling
        response = request.urlopen(self._url(stock_name))
        return response.read().decode('utf-8')

    def _parse_data(self, data, stock_name):
        quand_list = []
        try:
            entry_strings = data.split('\n')
            labels = entry_strings[0].split(',')
            print(labels)
            print('\n\n')
            for i in range(1, len(entry_strings)):
                entry_string = entry_strings[i]
                entries = entry_string.split(',')
                entry = {}
                counter = 0
                for label in labels:
                    entry[label] = entries[counter]
                    counter += 1
                quand = Quand(stock_name, entry)
                quand_list.append(quand)
        except IndexError as e:
            print(str(e))
        return quand_list

    def request_data(self, stock_name):
        data = self._make_request(stock_name)
        return self._parse_data(data, stock_name)

