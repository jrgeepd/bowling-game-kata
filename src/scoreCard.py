class ScoreCard:
    """
    ADT: ScoreCard
    Domain: Bowling
    """

    def __init__(self, score_card):
        self.rolls: list[int] = []
        self._parse_rolls(score_card)

    def get_rolls(self):
        return self.rolls

    # -----------------------
    # Rolls / Pins parsing
    # -----------------------

    def _parse_rolls(self, score_card):
        """
        Rolls:
        - X = Strike (10)
        - / = Spare (10 - previous roll)
        - - = Foul (0)
        - 0-9 = Pins
        """
        for ch in score_card:
            if ch == "X":                 # Strike
                self.rolls.append(10)

            elif ch == "-":               # Foul
                self.rolls.append(0)

            elif ch == "/":               # Spare
                self.rolls.append(10 - self.rolls[-1])

            else:                          # Pins
                self.rolls.append(int(ch))

    # -----------------------
    # Score (Frame logic)
    # -----------------------

    def score(self):
        score = 0
        roll = 0

        for frame in range(10):  # 10 Frames
            if self._is_strike(roll):
                score += 10 + self._strike_bonus(roll)
                roll += 1

            elif self._is_spare(roll):
                score += 10 + self._spare_bonus(roll)
                roll += 2

            else:
                score += self._frame_pins(roll)
                roll += 2

        return score

    # -----------------------
    # Frame helpers
    # -----------------------

    def _is_strike(self, i):
        return self.rolls[i] == 10

    def _is_spare(self, i):
        return self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i):
        return self.rolls[i + 1] + self.rolls[i + 2]

    def _spare_bonus(self, i):
        return self.rolls[i + 2]

    def _frame_pins(self, i):
        return self.rolls[i] + self.rolls[i + 1]
