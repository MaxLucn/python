import sys
import pygame
import constants
from game.plane import OurPlane


def main():
    """ 游戏入口 """
    # 初始化游戏
    pygame.init()

    # 屏幕的宽度与高度
    width, height = 480, 852

    # 设置屏幕
    screen = pygame.display.set_mode((width, height))
    # 设置窗口标题
    pygame.display.set_caption('飞机大战')

    # 游戏的背景图片
    bg_img = pygame.image.load(constants.BG_IMG)
    # 加载游戏标题
    game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    # 设置游戏标题位置
    game_title_rect = game_title.get_rect()
    game_title_width, game_title_height = game_title.get_size()
    game_title_rect.left = (width - game_title_width) / 2
    game_title_rect.top = height / 2 - game_title_height
    # 加载游戏开始按钮
    game_start = pygame.image.load(constants.IMG_GAME_START_BTN)
    # 设置游戏开始按钮的位置
    game_start_rect = game_start.get_rect()
    game_start_width, game_start_height = game_start.get_size()
    game_start_rect.left = (width - game_start_width) / 2
    game_start_rect.top = height / 2 + game_start_height

    # 加载游戏的背景音乐
    pygame.mixer.music.load(constants.BG_MUSIC )
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    # 游戏状态
    READY = 0  # 游戏准备中
    PLAYING = 1  # 游戏进行中
    status = READY

    # 控制帧数
    clock = pygame.time.Clock()
    frame = 0

    # 我方飞机
    our_plane = OurPlane(screen)

    while True:
        """ 循环事件 """
        frame += 1
        # 帧数率
        clock.tick(60)
        if frame > 60:
            frame = 0
        # 1.处理事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == READY:
                    status = PLAYING
            # 键盘事件
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    our_plane.move_up()
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    our_plane.move_down()
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    our_plane.move_left()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    our_plane.move_right()
                elif event.key == pygame.K_SPACE:
                    our_plane.shoot()

        if status == READY:
            """ 游戏准备中 """
            # 绘制背景图片
            screen.blit(bg_img, bg_img.get_rect())
            screen.blit(game_title, game_title_rect)
            screen.blit(game_start, game_start_rect)
        if status == PLAYING:
            """ 游戏进行中 """
            # 绘制背景图片
            screen.blit(bg_img, bg_img.get_rect())
            # 绘制我方飞机
            our_plane.update(frame)
            # 绘制敌方飞机
            # 绘制子弹
            our_plane.bullets.update()

        # 更新屏幕状态
        pygame.display.flip()


if __name__ == '__main__':
    main()
