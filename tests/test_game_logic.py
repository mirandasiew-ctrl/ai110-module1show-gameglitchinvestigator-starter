from logic_utils import check_guess, get_hint_message 
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
#FIX: Added tests for low highhint messages using AI
def test_too_high_hint_says_go_lower():
    # A guess above the secret must point the player DOWN, not up
    message = get_hint_message("Too High")
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_hint_says_go_higher():
    # A guess below the secret must point the player UP, not down
    message = get_hint_message("Too Low")
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_hint_direction_end_to_end():
    # Guessing 60 against a secret of 50 should tell the player to go LOWER
    assert "LOWER" in get_hint_message(check_guess(60, 50))
    # Guessing 40 against a secret of 50 should tell the player to go HIGHER
    assert "HIGHER" in get_hint_message(check_guess(40, 50))
