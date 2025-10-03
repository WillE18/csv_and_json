from urllib.request import Request, urlopen
import json

with open('authtoken.txt', 'r') as at:
    auth_token = at.read()

req = Request(f'https://api.football-data.org/v4/competitions/ELC/standings?season=2024')
req.add_header('X-Auth-Token', auth_token)
content = urlopen(req).read()
data_dict = json.loads(content)

season = data_dict['standings'][0]['table']

for team in season:
    print(f"{team['position']}. {team['team']['shortName']}")