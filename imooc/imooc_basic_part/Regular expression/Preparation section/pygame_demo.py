import pygame
import sys

# 初始化 pygame
pygame.init()
pygame.mixer.init()

size = width, height = 500, 500
speed = [5, 2]
black = 0, 20, 0

# 得到屏幕对象
screen = pygame.display.set_mode(size)
# 图片加载
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# 加载音乐
music = pygame.mixer.Sound('Super Mario Theme .wav')
# -1 无限循环
music.play(-1)

# 加入文字
# 有两种方法1、使用系统默认的字体进行加载，2、自己准备一个字体文件tff，放在项目同级目录下
fonts = pygame.font.get_fonts()
red = pygame.Color(245, 23, 34)
# print(fonts)
font = pygame.font.SysFont('pronw4ttc', 40)
text = font.render("I'm about to fall asleep", True, red)

# 游戏主循环
while 1:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # 更新游戏状态
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 在屏幕上进行绘制
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(text, (20, 20))
    pygame.display.flip()
