from bowling.Bowling import Bowling


def test_should_return_0_when_no_pin_down():
    bowling = Bowling()
    roll_many(bowling, 20, 0)
    assert bowling.score() == 0

def test_should_return_20_when_20_pin_down():
    bowling = Bowling()
    roll_many(bowling, 20, 1)
    assert bowling.score() == 20

def test_should_return_16_when_spare_and_3():
    bowling = Bowling()
    roll_many(bowling, 2, 5)
    bowling.roll(3)
    assert bowling.score() == 16

def test_should_return_26_when_strike_and_5_and_3():
    bowling = Bowling()
    bowling.roll(10)
    bowling.roll(5)
    bowling.roll(3)
    assert bowling.score() == 26

def test_should_return_300_when_full_strike():
    bowling = Bowling()
    roll_many(bowling, 11, 10)
    assert bowling.score() == 300

def roll_many(bowling, rolls, pin_down_by_roll):
    for roll in range(rolls):
        bowling.roll(pin_down_by_roll)
