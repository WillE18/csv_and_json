from urllib.request import Request, urlopen
import json

with open('spot_auths.json', 'r') as auths:
    obj = json.load(auths)
    token = obj['access_token']

liked_songs = []

for o in range(0, 950, 50): #i know i have 946 songs
    req = Request(f'https://api.spotify.com/v1/me/tracks?offset={o}&limit=50')
    req.add_header('Authorization', f'Bearer {token}')
    data = urlopen(req).read()
    converted_data = json.loads(data)['items']

    for song in converted_data:
        liked_songs.append({
            'name': song['track']['name'],
            'added_at': song['added_at'],
            'artists:': [artist['name'] for artist in song['track']['artists']],
            'url': song['track']['external_urls']['spotify']
        })
    print(f'{o+50} songs added so far')

with open('spotify_liked_songs.json', 'a') as file:
    json.dump(liked_songs, file, indent=2)