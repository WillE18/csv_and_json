class BMW_Data:
    def __init__(self, csv_file):
        self.file_name = csv_file
        self.data = self._get_sanitised_data()
        self.formatted_data = self._convert()
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
    def _convert(self):
        return list(map(self._dict_convert, self.data))
    def get_yearly_data(self, year):
        return [entry for entry in self.formatted_data if entry['Year'] == str(year)]
    def get_yearly_units_sold(self, year):
        yearly_data = self.get_yearly_data(year)
        return sum(int(item['Sales_Volume']) for item in yearly_data)

data = BMW_Data('sample_data/bmw_sales_data.csv')
print(data.get_yearly_units_sold(2024))

#Either the data is wrong, I'm misunderstanding the data, or something in my code is wrong

#The application performs all good, but it says that they, for example, sold 17,527,854 units in 2017.
#According to google, BMW sold 2.2 million cars so idk what's going on there.