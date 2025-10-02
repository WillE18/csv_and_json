import json

class Json_to_CSV:
    def __init__(self, json_file):
        self.file_name = json_file
    def _get_dict(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)
    def _get_header(self):
        all_keys = [list(item.keys()) for item in self._get_dict()]
        return list(self._get_dict()[0].keys()) #assumes all dicts have same keys
    def _get_items(self):
        return [list(item.values()) for item in self._get_dict()]
    def _format_line(self, line):
        line = [str(value) for value in line]
        return ','.join(line)+'\n'
    def convert_to_csv(self):
        with open(self.file_name.replace('.json', '.csv'), 'w') as f:
            f.write(self._format_line(self._get_header()))
            for item in self._get_items():
                f.write(self._format_line(item))

csver = Json_to_CSV('grocery_chain_data.json')
csver.convert_to_csv()