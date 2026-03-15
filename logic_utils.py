def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a given difficulty level.

    Args:
        difficulty: A string indicating the difficulty level.
            Expected values are "Easy", "Medium", or "Hard".

    Returns:
        A tuple of (low, high) integers representing the inclusive
        range of valid guesses for the selected difficulty.

    Raises:
        NotImplementedError: This function has not been refactored yet.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def parse_guess(raw: str):
    """Parse raw user input into a validated integer guess.

    Converts the raw string input from the user into an integer,
    performing validation to ensure the input is a valid number.

    Args:
        raw: The raw string input from the user's guess field.

    Returns:
        A tuple of (ok, guess_int, error_message) where:
            - ok (bool): True if the input was successfully parsed.
            - guess_int (int | None): The parsed integer,
              or None on failure.
            - error_message (str | None): A descriptive error,
              or None on success.

    Raises:
        NotImplementedError: This function has not been refactored yet.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def check_guess(guess: int, secret: int) -> str:
    """Compare the player's guess against the secret number.

    Determines whether the guess is correct, too high, or too low
    relative to the secret number.

    Args:
        guess: The player's guessed integer.
        secret: The target secret number to guess.

    Returns:
        A string outcome: "Win" if the guess matches, "Too High" if
        the guess exceeds the secret, or "Too Low" if it falls short.
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Calculate the updated score based on the round outcome.

    Awards or deducts points from the current score depending on
    whether the player won or made an incorrect guess, scaled by
    the attempt number.

    Args:
        current_score: The player's score before this round.
        outcome: The result of the guess ("Win", "Too High", or "Too Low").
        attempt_number: The current attempt count (1-indexed).

    Returns:
        The updated score as an integer.

    Raises:
        NotImplementedError: This function has not been refactored yet.
    """
    raise NotImplementedError(
        "Refactor this function from app.py into logic_utils.py"
    )


def reset_game() -> dict:
    """Return a fresh game state dictionary for starting a new round.

    Provides default values for all session state keys that need
    to be reset when the player starts a new game.

    Returns:
        A dictionary containing:
            - "attempts" (int): Reset to 0.
            - "status" (str): Set to "playing".
            - "history" (list): An empty list of past guesses.
    """
    return {
        "attempts": 0,
        "status": "playing",
        "history": [],
    }
