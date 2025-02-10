from random import choice


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'ang mo kio' in lowered:
        return choice(['Brew & Co.', 'Ang Mo Kio Park', 'AMK Hub'])
    else:
        return choice(['bye', 'see ya!'])