DOWN = 0
RIGHT = 1
UP = 2
LEFT = 3
def randomRect():
    return Rect(randint(1, xBound - 2) * blockSize, randint(1, yBound - 2) * blockSize, blockSize, blockSize)

apple = randomRect()


# Direction traveled is encoded as an integer.
# 0 - DOWN | 1 - RIGHT | 2 - UP | 3 - LEFT
direction = RIGHT

# The size of a single block
blockSize = 50


if hasEaten:
    apple= apple-2


# The maximum number of blocks on each side.
xBound = 30
yBound = 30
