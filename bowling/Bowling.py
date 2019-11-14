
class Bowling:

    def __init__(self):
        self.rolls = [0 for i in range(22)]
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        score = 0
        roll_position = 0
        for frame in range(11):
            if self.is_strike(roll_position):
                score += 10 + self.score_strike_bonus(roll_position)
                roll_position += 1
            elif self.is_spare(roll_position):
                score += 10 + self.score_spare_bonus(roll_position)
                roll_position += 2
            else:
                score += self.score_frame(roll_position)
                roll_position += 2

        return score

    def score_frame(self, current_index):
        return self.rolls[current_index] \
               + self.rolls[current_index + 1]

    def score_strike_bonus(self, roll_position):
        return self.rolls[roll_position + 1] \
               + self.rolls[roll_position + 2]

    def score_spare_bonus(self, current_index):
        return self.rolls[current_index + 2]

    def is_spare(self, current_index):
        return self.score_frame(current_index) == 10

    def is_strike(self, current_index):
        return self.rolls[current_index] == 10

