"""飞机大战分析
步骤：
面向对象项目分析
项目初始化
载入我方飞机
载入敌方飞机
大型敌机
碰撞检测，爆炸效果及音效
游戏成绩统计
优化
"""
import pygame
import sys

import constants
from game.plane import OurPlane, SmallEnemyPlane
from store.result import PlayRest


class PlaneWar(object):
    """ 飞机大战 """

    # 游戏准备中
    READY = 0
    # 正在游戏当中
    PLAYING = 1
    # 游戏结束
    OVER = 2

    # 游戏状态。0 准备中、1 游戏中、2 游戏结束
    status = 0

    our_plane = None
    # 播放帧数
    frame = 0

    # 一架飞机可以属于多个精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # 游戏结果
    rest = PlayRest()

    def __init__(self):
        # 初始化游戏
        pygame.init()
        self.width, self.height = 480, 852
        # 屏幕对象
        self.screen = pygame.display.set_mode((self.width, self.height))
        # 设置窗口标题
        pygame.display.set_caption('小蜜蜂')

        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)

        # 游戏的标题
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # 游戏标题的高、宽度
        t_width, t_height = self.img_game_title.get_size()
        self.img_game_title_rect.topleft = (int((self.width - t_width) / 2),
                                            int(self.height / 2 - t_height))
        # 开始按钮
        self.btn_start = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.btn_start_rect = self.btn_start.get_rect()
        self.btn_width, btn_height = self.btn_start.get_size()
        self.btn_start_rect.topleft = (int((self.width - self.btn_width) / 2),
                                       int(self.height / 2 + btn_height))

        # 游戏文字对象
        self.score_font = pygame.font.SysFont('pronw4ttc', 32)

        # 加载背景音乐
        music = pygame.mixer.Sound(constants.BG_MUSIC)
        # 无限循环播放
        music.play(-1)
        # 调节音量
        pygame.mixer.music.set_volume(0.1)

        # 我方飞机对象
        self.our_plane = OurPlane(self.screen, speed=6)
        self.clock = pygame.time.Clock()

        # 上次按的键盘的某一个键，用于控制飞机的移动
        self.key_down = None

    def bind_event(self):
        """ 绑定事件 """

        # 监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                # 游戏正在准备中，点击才能进入游戏
                if self.status == self.READY:
                    self.status = self.PLAYING
                elif self.status == self.OVER:
                    self.status = self.READY
                    self.add_small_enemies(6)
            elif event.type == pygame.KEYDOWN:
                # 键盘事件
                self.key_down = event.key
                # 正在游戏中，才需要控制见键盘 ASWD
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        # 发射子弹
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        # 随机添加 num 架敌人小型飞机
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 4)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        """ 游戏主循环部分 """
        while True:
            # 1、设置帧速率
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                self.frame = 0
            # 2、绑定事件
            self.bind_event()

            # 3、更新游戏状态
            if self.status == self.READY:
                # 游戏正在准备中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 游戏的标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # 开始按钮
                self.screen.blit(self.btn_start, self.btn_start_rect)
                self.key_down = None
            elif self.status == self.PLAYING:
                # 游戏进行中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制飞机
                self.our_plane.update(self)
                # 绘制子弹
                self.our_plane.bullets.update(self)
                # 绘制敌人小型飞机
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render('score：{0}'.format(self.rest.score),
                                                    False, constants.TEXT_SCORE_COLOR)
                self.screen.blit(score_text, score_text.get_rect())
            elif self.status == self.OVER:
                # 游戏结束
                # 绘制结束背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())

                # 分数统计
                # 绘制本次总分
                score_text = self.score_font.render('{0}'.format(self.rest.score),
                                                    False, constants.TEXT_SCORE_COLOR)
                score_text_rect = score_text.get_rect()
                text_w = score_text.get_size()[0]
                text_h = score_text.get_size()[1]
                # 改变文字位置
                score_text_rect.topleft = (int((self.width - text_h) / 2),
                                           int(self.height / 2))
                self.screen.blit(score_text, score_text_rect)
                # 历史最高分
                score_history = self.score_font.render(
                    '{0}.'.format(self.rest.get_max_score()), False, constants.TEXT_SCORE_COLOR)
                self.screen.blit(score_history, (150, 40))

            pygame.display.flip()
