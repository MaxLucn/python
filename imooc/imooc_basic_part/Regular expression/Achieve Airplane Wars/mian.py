import sys

import pygame
import constants
from game.plane import OurPlane, SmallEnemyPlane
from game.war import PlaneWar


def main():
    """ 游戏入口， main 方法 """
    war = PlaneWar()
    # 添加小型敌机 6 架
    war.add_small_enemies(6)
    war.run_game()


if __name__ == '__main__':
    main()
