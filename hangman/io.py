from hangman import game

def prompt_guess() -> str:
    """Receives a guess letter from the user and return it"""
    guess = input(f'guess a letter includes in the secret word: ')
    return guess


def print_status(state: dict) -> None:
    """display word to guess state, guessed, letters and remaining attempts"""
    print(f'The correct guesses:  {game.render_display(state)}\n'
          f'The guessed letters are:  {" ".join(state['guessed'])}\n'
          f'Number of attempts remaining:  {state['max_tries'] - state['wrong_guesses']}\n')


def print_result(state: dict) -> None:
    """display win/loss message and all result in the end of the game"""
    if game.is_won(state):
        print(f'======You are the champion, you guessed it======\n'
              f'{game.render_summary(state)}\n'
              f'Wrong guesses:  {state['wrong_guesses']}\n')
    if game.is_lost(state):
        print(f'======Loser, try again======\n'
              f'{game.render_summary(state)}\n'
              f'Wrong guesses:  {state['wrong_guesses']}\n')
