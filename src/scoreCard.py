class ScoreCard:
    """
    ADT: ScoreCard
    Domain: Bowling
    """

    def __init__(self, notation: str):
        self.rolls: list[int] = []
        self._parse_rolls(notation)

    # -----------------------
    # Rolls / Pins parsing
    # -----------------------

    def _parse_rolls(self, notation: str) -> None:
        """
        Rolls:
        - X = Strike (10)
        - / = Spare (10 - previous roll)
        - - = Foul (0)
        - 0-9 = Pins
        """
        for ch in notation:
            if ch in (" ", "|"):
                continue

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

    def score(self) -> int:
        score = 0
        roll_index = 0

        for frame in range(10):  # 10 Frames
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1

            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2

            else:
                score += self._frame_pins(roll_index)
                roll_index += 2

        return score

    # -----------------------
    # Frame helpers
    # -----------------------

    def _is_strike(self, i: int) -> bool:
        return self.rolls[i] == 10

    def _is_spare(self, i: int) -> bool:
        return self.rolls[i] + self.rolls[i + 1] == 10

    def _strike_bonus(self, i: int) -> int:
        return self.rolls[i + 1] + self.rolls[i + 2]

    def _spare_bonus(self, i: int) -> int:
        return self.rolls[i + 2]

    def _frame_pins(self, i: int) -> int:
        return self.rolls[i] + self.rolls[i + 1]