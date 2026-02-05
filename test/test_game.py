import pytest

from src.scoreCard import ScoreCard


@pytest.mark.state_n
def test_hitting_pins_regular():
    # Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    assert score_card.score() == total


@pytest.mark.state_n
def test_symbol_zero():
    # test symbol -
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
    assert score_card.score() == total

    pins = "9-3561368153258-7181"
    total = 82
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [9, 0, 3, 5, 6, 1, 3, 6, 8, 1, 5, 3, 2, 5, 8, 0, 7, 1, 8, 1]
    assert score_card.score() == total


@pytest.mark.spare
def test_spare_not_extra():
    # test spare not extra
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [9, 0, 3, 7, 6, 1, 3, 7, 8, 1, 5, 5, 0, 10, 8, 0, 7, 3, 8, 0]
    assert score_card.score() == total


@pytest.mark.strike
def test_strike():
    # test strike
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
    assert score_card.score() == total

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 9, 0, 10, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
    assert score_card.score() == total


@pytest.mark.strike
def test_two_strikes():
    # two strikes in a row is a double
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 10, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
    assert score_card.score() == total


@pytest.mark.strike
def test_three_strikes():
    # three strikes in a row is a triple
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 10, 10, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0]
    assert score_card.score() == total


@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    # one pin in extra roll
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [9, 0, 3, 7, 6, 1, 3, 7, 8, 1, 5, 5, 0, 10, 8, 0, 7, 3, 8, 2, 8]
    assert score_card.score() == total

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert score_card.score() == total


@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    # two strikes in extra rolls
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 10, 10, 10]
    assert score_card.score() == total


@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    # one strike in extra roll
    pins = "8/549-XX5/53639/9/X"
    total = 149
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [8, 2, 5, 4, 9, 0, 10, 10, 5, 5, 5, 3, 6, 3, 9, 1, 9, 1, 10]
    assert score_card.score() == total


@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    # spare in extra roll
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 5, 5, 10, 5, 5, 10, 10, 5, 5, 0, 0, 5, 5, 10, 5, 5]
    assert score_card.score() == total


@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    # 12 strikes is a “Thanksgiving Turkey”
    pins = "XXXXXXXXXXXX"
    total = 300
    score_card = ScoreCard(pins)
    assert score_card.get_rolls() == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert score_card.score() == total
