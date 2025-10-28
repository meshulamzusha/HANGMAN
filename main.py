from data.words import secret_words
from hangman import io, game
from hangman.words import choose_secret_word

def play(words: list[str], max_tries: int = 20) -> None:
    secret = choose_secret_word(words).casefold()
    print(secret)
    state = game.init_state(secret, max_tries)

    while not game.is_won(state) and not game.is_lost(state):
        guess = io.prompt_guess()
        is_valid = game.validate_guess(guess, state)

        print(is_valid[1])

        if is_valid[0]:
            game.apply_guess(state, guess)
            io.print_status(state)

        io.print_result(state)

if __name__ == "__main__":
    play(secret_words)