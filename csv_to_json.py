import json

class CSV_To_Json:
    def __init__(self, csv_file):
        self.file_name = csv_file
    def _sanitise(self, line):
        return line.replace('\n', '').split(',')
    def _get_sanitised_data(self):
        with open(self.file_name, 'r') as f:
            return [self._sanitise(line) for line in f.readlines()][1:] #get rid of header cause you get that seperately
    def _get_header(self):
        with open(self.file_name, 'r') as f:
            return self._sanitise(f.readline())
    def _dict_convert(self, entry):
        header = self._get_header()
        dict = {}
        for i in range(0, len(entry)):
            dict[header[i]] = entry[i]
        return dict
    def _get_converted_data(self):
        return list(map(self._dict_convert, self._get_sanitised_data()))
    def convert_to_json(self):
        with open(self.file_name.replace('.csv', '.json'), 'w') as f:
            json.dump(self._get_converted_data(), f, indent=2)

jsoner = CSV_To_Json('bmw_sales_data.csv')
jsoner.convert_to_json()