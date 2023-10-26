#probability with python via Codecademy!

import numpy as np
from matplotlib import pyplot as plt

# Let's say we have a normal six-sided die.
# We can simulate the result of rolling the die with:
# np.random.randint(1, 7)
# The first argument is the lowest number possible to be rolled.
# The second argument is the highest number possible to be rolled (plus one).
# So in this case, the die can land on any number between 1 and 6 (inclusive).
# We can use this function to simulate rolling a die multiple times.
# For example, this code:
# rolls = np.random.randint(1, 7, 100)
# simulates rolling a six-sided die 100 times.
# The result of each roll is stored in rolls.
# We can use plt.hist to display the results of a simulation.
# plt.hist(rolls, bins=6)
# simulates rolling a six-sided die 100 times, and then displays a histogram of the results.
# The bins argument tells plt.hist how many bars to display.
# In this case, there will be a bar for each possible number that the die could land on (1 through 6).