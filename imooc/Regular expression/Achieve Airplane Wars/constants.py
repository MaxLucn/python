import os
import pygame

# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 静态文件的目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'image_/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'image_/game_over.png')
# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'image_/game_title.png')
# 开始游戏的按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'image_/game_start.png')

# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'music-/game_bg_music.wav')
# 游戏分数颜色
TEXT_SCORE_COLOR = pygame.Color(255, 244, 0)
# 击中小型飞机加10份
SCORE_SHOOT_SMALL = 10
# 游戏结果存储的文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rest.txt')

# 我方飞机的静态资源
OUR_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'image_/hero1.png'),
                      os.path.join(ASSETS_DIR, 'image_/hero2.png')]
OUR_DESTROY_IMG_LIST = [os.path.join(ASSETS_DIR, 'image_/hero_broken_n1.png'),
                        os.path.join(ASSETS_DIR, 'image_/hero_broken_n2.png'),
                        os.path.join(ASSETS_DIR, 'image_/hero_broken_n3.png'),
                        os.path.join(ASSETS_DIR, 'image_/hero_broken_n4.png'),
                        ]

# 子弹的图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'image_/bullet1.png')
# 子弹发射的音效
BULLET_SHOOT_SOUND = os.path.join(ASSETS_DIR, 'music-/bullet.wav')
# 敌人小型飞机的图片和音效
SMALL_ENEMY_PLANE_IMG = os.path.join(ASSETS_DIR, 'image_/enemy1.png')
SMALL_ENEMY_DES_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'image_/enemy1_down1.png'),
                                  os.path.join(ASSETS_DIR, 'image_/enemy1_down2.png'),
                                  os.path.join(ASSETS_DIR, 'image_/enemy1_down3.png'),
                                  os.path.join(ASSETS_DIR, 'image_/enemy1_down4.png'),
                                  ]
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(ASSETS_DIR, 'music-/enemy1_down.wav')
