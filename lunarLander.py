
# 1 turn = 1 second
# altitude in metres above the moon
altitude = 1000
# velocity toward the moon in metres/second. Negative if moving away
velocity = 0
# fuel in litres
fuel = 1000
# velocity increases by 1.6 metres/second, due to the acceleration of gravity
# velocity decreases by an amount proportional to the amount of fuel you
# just burned (zero at the first turn).

# safe landing occurs if your speed is under 10 meters/second

# After each game, ask the user if they want to play again. Any response that
# begins with 'y' or 'Y' means "yes," any response that begins with 'n' or 'N'
# means "no," and for any other answer you should ask again