import constants


class PlayRest(object):
    """ 玩家的结果统计 """
    # 总分
    __score = 0
    # 生命数量
    __life = 3
    # 生命值
    __blood = 1000

    @property
    def score(self):
        """ 单词游戏分数 """
        return self.__score

    @score.setter
    def score(self, value):
        """ 设置游戏分数 """
        if value < 0:
            return None
        self.__score = value

    def set_history(self):
        """ 记录最高分 """
        # 读取文件中的存储数据
        # 新的分数与文件中的分数比较，如果大于文件中的分数则存储，如果小于文件中的值则忽略
        # 存储分数的时候采取替换的模式w，不可以采取追加的模式a+
        if int(self.get_max_score()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w') as f:
                f.write('{0}'.format(self.score))

    def get_max_score(self):
        """ 读取文件中的历史最高分 """
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r') as f:
            r = f.read()
            if r:
                rest = r
        return rest
