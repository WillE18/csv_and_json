from urllib.request import urlopen
import json

allowed_answers = {
    'Walter White': ['walter', 'walt', 'mr white', 'walter white', 'heisenberg'],
    'Saul Goodman': ['saul', 'saul goodman', 'jimmy', 'jimmy mcgill'],
    'Skyler White': ['mrs white', 'skylar white', 'skyler white', 'skyler', 'skylar'],
    'Jesse Pinkman': ['jesse', 'jesse pinkman', 'pinkman', 'jessie', 'jessie pinkman'],
    'Gustavo Fring': ['mr fring', 'fring', 'gus', 'gustavo fring', 'gus fring'],
    'Hank Schrader': ['hank', 'hank shrader', 'hank schrader'],
    'Marie Schrader': ['marie', 'marie schrader', 'marie shrader'],
    'Mike Ehrmantraut': ['mike', 'mike ehrmantraut', 'ehrmantraut'],
    'Todd': ['todd', 'tod'],
    'Tio Salamanca': ['hector', 'hector salamanca', 'tio', 'tio salamanca', 'don hector'],
    'Uncle Jack': ['jack', 'uncle jack'],
    'Gale Boetticher': ['gale', 'gale boetticher', 'gail boetticher', 'gail'],
    'The fly': ['fly', 'the fly'],
    'Badger': ['badger']
}

def check_answer(answer, guess):
    return guess.strip().lower() in allowed_answers[answer]

invalid_authors = ['Stephen King'] #for some reason the api returns a stephen king quote lmao

valid_quote = False
while not valid_quote:
    link = urlopen('https://api.breakingbadquotes.xyz/v1/quotes')
    quote_obj = json.loads(link.read())[0]
    quote, author = quote_obj.values()
    if author not in invalid_authors:
        valid_quote = True

print('Welcome to guess the Breaking Bad quote!')
print(quote)
choice = input('Who said it? ')
if check_answer(author, choice):
    print(f'Well done, you guessed correctly. It was {author}')
else:
    print(f'Unlucky! The answer was {author}') 

