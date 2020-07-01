import sys
import pygame

pygame.init()

size = width, height = 500, 500
speed = [5, 2]
black = 0, 0, 255

# 得到屏幕对象
screen = pygame.display.set_mode(size)
# 图片加载
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()


class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


# 实例化精灵
sprite_1 = Block(pygame.Color(255, 0, 0), 50, 50)

# 游戏主循环
while True:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(sprite_1.image, sprite_1.rect)
    # screen.display.flip()
    pygame.display.flip()
