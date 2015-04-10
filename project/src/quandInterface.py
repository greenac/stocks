import urllib.request as request
import urllib.error as url_error
from src.quand import Quand
from socket import timeout
import json

class QuandInterface:
    def __init__(self):
        self._api_key = 'SDnxkRiZzVHTFrVgWRR4'
        self.quands = {}

    def _url(self, stock_name):
        return 'https://www.quandl.com/api/v1/datasets/WIKI/' \
                     + stock_name + '.csv?auth_token=' + self._api_key

    def _make_request(self, stock_name):
        # TODO -- add error handling
        try:
            response = request.urlopen(self._url(stock_name))
            return response.read().decode('utf-8')
        except (url_error.HTTPError, url_error.URLError) as e:
            print('error getting quand: ', stock_name, str(e))
        except timeout:
            print('timeout getting stock: ' + stock_name)
        return None

    def _parse_data(self, data, stock_name):
        quand_list = []
        try:
            entry_strings = data.split('\n')
            labels = entry_strings[0].split(',')
            for i in range(1, len(entry_strings)):
                entry_string = entry_strings[i]
                entries = entry_string.split(',')
                entry = {}
                counter = 0
                if len(labels) == len(entries):
                    for label in labels:
                        entry[label] = entries[counter]
                        counter += 1
                    quand = Quand(stock_name, entry)
                    quand_list.append(quand)
            self.quands[stock_name] = quand_list
        except IndexError as e:
            print(str(e))
        return None

    def request_data(self, stock_name):
        data = self._make_request(stock_name)
        if data:
            print('received data for: ', stock_name)
            self._parse_data(data, stock_name)
        else:
            print('did not received data for: ', stock_name)
        return None

    def write_quands_to_file(self):
        for stock_name, quand_list in self.quands.items():
            quand_dicts_list = []
            for quand in quand_list:
                quand_dicts_list.append(quand.as_dict())
            try:
                file_path = 'files/quand_files/' + stock_name + '.json'
                with open(file_path, 'w') as quand_file:
                    json.dump(quand_dicts_list, quand_file)
                quand_file.close()
            except Exception as e:
                print('error opening quand file: ' + str(e))
        return None


