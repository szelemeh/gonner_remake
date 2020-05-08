from sprites.enemies.enemy import *


class GroundEnemy(Enemy):
    def __init__(self, x, y, width, height, target):
        super().__init__(x, y, width, height, target)

    def update(self):
        if self.vel_x > 0:
            self.images = self.images_right
        else:
            self.images = self.images_left

        Enemy.apply_gravity(self)

        Enemy.update(self)
