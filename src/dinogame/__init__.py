from arcade import color

# Sizes
SCREEN_WIDTH = 1510
SCREEN_HEIGHT = 800

# Window constraints
X_MIN = 10
X_MAX = SCREEN_WIDTH - 10
Y_MIN = 10
Y_MAX = SCREEN_HEIGHT - 10

# GUI
FONT_SIZE = 20
FONT_LINE_HEIGHT = FONT_SIZE * 2

# (Enemy) spawning constraints
SPAWN_MIN_X = X_MAX
SPAWN_MAX_X = 2*X_MAX

# Enemy data
ENEMY_TYPES = [
    {
        'image': './resources/enemies/bird.png',
        'sy': 100,  # Make birds appear at three different heights
        'vx': 0,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    },
    {
        'image': './resources/enemies/bird.png',
        'sy': 170,  # Make birds appear at three different heights
        'vx': 0,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    },
    {
        'image': './resources/enemies/bird.png',
        'sy': 232,  # Make birds appear at three different heights
        'vx': 0,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    },
    {
        'image': './resources/enemies/cactus.png',
        'sy': 100,
        'vx': 0,
        'vy': 0,
        'ax': 0,
        'ay': 0,
    }
]

# Game constants
GROUND_HEIGHT = 100
JUMP_VELOCITY = 25
GRAVITY = -1
PLAYER_X = 150
PLAYER_VX = 8
CUTOFF = 100
# DOUBLE_JUMP_MARGIN = 1 # Only if we allow double jumping

# Colors
BACKGROUND_COLOR = color.ALMOND
# Names
SCREEN_TITLE = "DinoGame"
# Counts
MAX_ENEMY_COUNT = 3

# DEBUG
DEBUG = False
TIMINGS_COUNTER = 1000

# AI

AI = True
