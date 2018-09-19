# Lunar Lander

You are in a lunar module, some distance above the Moon's surface.
Gravity is pulling you toward the Moon at an ever-increasing rate of
speed. You have a limited amount of fuel to use, and each time you burn
fuel, you reduce your speed by a certain amount. If you burn the right
amount of fuel at the right time, you can land safely (that is, when you
reach the Moon's surface, you are not
going *too* fast).

Game
=========

This game is not timed; you can take as long as you want to enter
numbers. Each time you enter a number, one second of "game time" will
have passed. In other words, 1 turn = 1 second.

At each turn, you are told:

-   Your **altitude** in metres above the moon
-   Your **velocity** toward the Moon in metres/second (this number will be negative if you are moving away)
-   How much **fuel** you have remaining (in litres)

You then get to specify:

-   How much **fuel** to burn
    -   Zero is a legal value (and may be all you have!)
    -   If you ask to burn more fuel than you have, burn all that you have
    -   If you ask to burn a negative amount of fuel, it should be treated as zero
- The game ends when your altitude becomes zero or negative. 
	- A *safe* landing occurs if your speed is under 10 meters/second. 
	- Otherwise, you blast a new crater in the moons surface.

