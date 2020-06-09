import constants
import pygame

from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """
    飞机基础类
    """
    # 飞机的图片
    plane_images = []

    # 飞机状态, True:飞机存活, False:飞机坠毁
    active = True

    # 子弹精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        self.speed = speed or 10
        self.img_list = []

        self.load_src()
        # 飞机的初始位置
        self.rect = self.img_list[0].get_rect()
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        self.width, self.height = self.screen.get_size()
        self.rect.left = (self.width - self.plane_w) / 2
        self.rect.top = self.height / 2

    def load_src(self):
        """ 加载飞机的图片到实例上 """
        for img in self.plane_images:
            self.img_list.append(pygame.image.load(img))

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """ 飞机向上移动 """
        self.rect.top -= self.speed

    def move_down(self):
        """ 飞机向下移动 """
        self.rect.top += self.speed

    def move_left(self):
        """ 飞机向左移动 """
        self.rect.left -= self.speed

    def move_right(self):
        """ 飞机向右移动 """
        self.rect.left += self.speed

    def shoot(self):
        """发射子弹"""
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)


class OurPlane(Plane):
    """ 我方飞机类 """
    plane_images = constants.OUR_PLANE_IMG_LIST

    def update(self, frame):
        """更新飞机的动画效果"""
        if frame % 5:
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)

    def move_up(self):
        super().move_up()
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        super().move_down()
        if self.rect.top > (self.height - self.plane_h):
            self.rect.top = (self.height - self.plane_h)

    def move_left(self):
        super().move_left()
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        super().move_right()
        if self.rect.left > self.width - self.plane_w:
            self.rect.left = self.width - self.plane_w
