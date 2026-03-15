from logic_utils import check_guess, reset_game

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug 1 fix: guess above secret must return "Too High" (not "Too Low") ---

def test_high_guess_is_too_high():
    # Guess of 99 against secret of 1 — should always be "Too High"
    result = check_guess(99, 1)
    assert result == "Too High"

def test_low_guess_is_too_low():
    # Guess of 1 against secret of 99 — should always be "Too Low"
    result = check_guess(1, 99)
    assert result == "Too Low"


# --- Bug 3 fix: new game must reset status so the player can play again ---

def test_new_game_status_is_playing():
    # After a reset, status must be "playing" so the game isn't blocked
    state = reset_game()
    assert state["status"] == "playing"

def test_new_game_clears_attempts():
    state = reset_game()
    assert state["attempts"] == 0

def test_new_game_clears_history():
    state = reset_game()
    assert state["history"] == []
