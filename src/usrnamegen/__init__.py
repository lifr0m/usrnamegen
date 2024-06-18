import random
from pathlib import Path


_ROOT = Path(__file__).parent


def generate_username() -> str:
    noun_list = (_ROOT / 'words/nouns.txt').read_text().split('\n')
    adjective_list = (_ROOT / 'words/adjectives.txt').read_text().split('\n')
    censored = (_ROOT / 'words/blacklist.txt').read_text().split('\n')

    while True:
        adjective = random.choice(adjective_list)
        noun = random.choice(noun_list)
        if adjective in censored or noun in censored:
            continue
        adjective = adjective.title()
        noun = noun.title()
        return f'{adjective}{noun}{random.randint(1, 99)}'
