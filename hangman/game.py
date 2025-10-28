def init_state(secret: str, max_tries: int) -> dict:
    """initialize a game state dict needed for game logic management"""
    return {
        'secret': secret,
        'display': ['_'] * len(secret),
        'guessed': set(),
        'wrong_guesses': 0,
        'max_tries': max_tries
    }


def validate_guess(guess: str, guessed: set[str]) -> tuple[bool, str]:
    """Returns a bool for the guess validation and an appropriate message"""
    if not guess.isalpha() or len(guess) > 1:
        is_valid = False
        message = "The guess must be only one letter."

        return is_valid, message

    if guess in guessed:
        is_valid = False
        message = f'The letter {guess} has already been guessed.'

    else:
        is_valid = True
        message = f'The letter {guess} has entered the list of guesses.'

    return is_valid, message


def apply_guess(state: dict, ch: str) -> bool:
    """if the guess is valid (see validate_guess()) update the state
    whether the guess is correct or not"""
    secret = state['secret']
    state['guessed'].add(ch)

    if ch in secret:
        for i in range(0, len(secret)):
            if ch == secret[i]:
                state['display'][i] = ch

        return True

    else:
        state['wrong_guesses'] += 1

        return False


def is_won(state: dict) -> bool:
    """Returns True if was able to guess the entire word else False"""
    return state['secret'] == "".join(state['display']) and state['wrong_guesses'] <= state['max_tries']


def is_lost(state: dict) -> bool:
    """Returns True if the user spend the max guess tries else False"""
    return state['secret'] != "".join(state['display']) and state['wrong_guesses'] >= state['max_tries']


def render_display(state: dict) -> str:
    """Returns the current state of guessed letters"""
    return " ".join(state['display'])


def render_summary(state: dict) -> str:
    """Returns the finally summary of guesses + secret"""
    return (f'The secret word is: {"".join(state['secret'])}\n'
            f'your guesses are: {state['guessed']}')
