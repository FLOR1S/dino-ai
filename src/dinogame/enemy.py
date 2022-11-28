import arcade
from random import randint
from dinogame import CUTOFF, X_MIN, X_MAX, GROUND_HEIGHT, ENEMY_TYPES, SPAWN_MIN_X, SPAWN_MAX_X


class Enemy(arcade.Sprite):
    """Player object (probably a dinosaur)"""

    def __init__(self, type=0, enemies_list=None):
        # Choose enemy type
        self.type = randint(0, len(ENEMY_TYPES)-1)
        # self.type = type

        if enemies_list is not None:
            spawn_min_x = max(SPAWN_MIN_X, min(enemies_list[-1].sx + 750, SPAWN_MAX_X))
        else:
            spawn_min_x = SPAWN_MIN_X

        super().__init__(ENEMY_TYPES[self.type]['image'], scale=0.5)

        # Set physics
        self.dt = 1.0
        self.sx = randint(spawn_min_x, SPAWN_MAX_X) + self.width/2
        # self.sx = SPAWN_MIN_X + self.width/2
        self.sy = ENEMY_TYPES[self.type]['sy'] + self.height/2
        self.vx = ENEMY_TYPES[self.type]['vx']
        self.vy = ENEMY_TYPES[self.type]['vy']
        self.ax = ENEMY_TYPES[self.type]['ax']
        self.ay = ENEMY_TYPES[self.type]['ay']

        # Update sprite location
        self.center_x = self.sx
        self.center_y = self.sy

    def translate(self, ds: tuple):
        self.sx = self.sx + ds[0]
        self.sy = self.sy + ds[1]

        # Remove if passed
        if self.sx < CUTOFF - self.width/2:
            self.kill()

        # Update sprite location
        self.center_x = self.sx
        self.center_y = self.sy

    def update(self):
        """Check for collisions and update player state accordingly
        """
        # Apply physics (euler) manually
        self.vx = self.vx + self.ax * self.dt
        self.vy = self.vy + self.ay * self.dt
        self.sx = self.sx + self.vx * self.dt
        self.sy = self.sy + self.vy * self.dt

        # TODO: Probably not necessary...
        # Handle ground
        if self.sy < GROUND_HEIGHT + self.height/2:
            self.sy = GROUND_HEIGHT + self.height/2

        self.center_x = self.sx
        self.center_y = self.sy
