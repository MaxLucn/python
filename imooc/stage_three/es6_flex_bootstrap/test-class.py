# coding:utf-8
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '点的位置({0}, {1})'.format(self.x, self.y)

if __name__ == '__main__':
    p = Point(1, 2)
    print(p)