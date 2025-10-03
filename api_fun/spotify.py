from urllib.request import Request, urlopen
import json

with open('spot_auths.json', 'r') as auths:
    obj = json.load(auths)
    token = obj['access_token']

offset = 0
liked_songs = []

complete = False
while not complete:
    req = Request(f'https://api.spotify.com/v1/me/tracks?offset={offset}&limit=50')
    req.add_header('Authorization', f'Bearer {token}')
    data = urlopen(req).read()
    converted_data = json.loads(data)['items']

    if len(converted_data) == 0:
        complete = True

    for song in converted_data:
        liked_songs.append({
            'name': song['track']['name'],
            'added_at': song['added_at'],
            'artists:': [artist['name'] for artist in song['track']['artists']],
            'url': song['track']['external_urls']['spotify']
        })
    
    offset += 50

    print(f'Songs added.')

with open('spotify_liked_songs.json', 'a') as file:
    json.dump(liked_songs, file, indent=2)

