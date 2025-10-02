import json

class CSV_to_Dict:
    def __init__(self, csv_file):
        self.file_name = csv_file
        self.data = self._get_sanitised_data()
        self.formatted_data = self._convert_data()
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
    def _convert_data(self):
        return list(map(self._dict_convert, self.data))
    def _jsonify(self, data):
        return json.dumps(data, indent=2)

class Spotify(CSV_to_Dict):
    def __init__(self, csv_file):
        super().__init__(csv_file)
    def get_user_count(self):
        return len(self.formatted_data)
    def get_from_ages(self, min, max=None, jsonify=True):
        max = min if max is None else max #if only given minimum, returns only that age
        data = [user for user in self.formatted_data if int(user['age']) >= int(min) and int(user['age']) <= int(max)]
        if jsonify:
            return self._jsonify(data)
        return data
    def get_all_ages(self, duplicates=False):
        all_ages = [int(user['age']) for user in self.formatted_data]
        if duplicates:
            return all_ages
        return sorted(list(dict.fromkeys(all_ages)))
        #dicts can't have duplicates, so converting to dictionary and then back to list removes duplicates
    def get_average_age(self):
        all_ages = self.get_all_ages(duplicates=True)
        return round(sum(all_ages)/self.get_user_count())
    def get_partial_data(self, header_items, jsonify=True):
        data = [{key:user[key] for key in user if key in header_items} for user in self.formatted_data]
        if jsonify:
            return self._jsonify(data)
        return data
    def get_average_songs_per_day(self):
        total = sum(int(user['songs_played_per_day']) for user in self.formatted_data)
        return round(total/self.get_user_count())
    
spotify = Spotify('sample_data/spotify_churn_dataset.csv')
print(spotify.get_from_ages(16, 34))
print(spotify.get_from_ages(48, jsonify=False))
print(spotify.get_average_age())
print(spotify.get_partial_data(['user_id', 'age', 'gender']))
print(spotify.get_average_songs_per_day())