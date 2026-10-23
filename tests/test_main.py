from main import respond


def test_echo():
    assert respond("привет") == "Вы сказали: привет"


def test_strips_spaces():
    assert respond("  hi  ") == "Вы сказали: hi"


def test_empty_input():
    assert respond("   ") == "Напишите что-нибудь 🙂"


def test_help():
    assert "help" in respond("help")
