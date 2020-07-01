class Student(object):
    """ 学生类 """
    def __init__(self, name, s_number):
        """
        构造函数
        :param name: 姓名
        :param s_number: 学号
        """
        self.name = name
        self.s_number = s_number
        self.s_course = []

    @property
    def course_detail(self):
        """ 返回课程 """
        return self.s_course

    def add_course(self, cour_info):
        """ 实现添加课程信息（cour_info）至学生对象的已选课程属性 """
        self.s_course.append(cour_info)

    def __str__(self):
        print('name: {0}, s_number: {1}'.format(self.name, self.s_number))


class Teacher(object):
    """ 教师类 """
    def __init__(self, t_number, t_name, t_phone):
        """
        构造函数
        :param t_number: 教师编号
        :param t_name: 教师姓名
        :param t_phone: 教师手机号
        """
        self.t_number = t_number
        self.t_name = t_name
        self.t_phone = t_phone

    def __str__(self):
        print('t_number: {0}, t_name: {1}'.format(self.t_number, self.t_name))


class Course(object):
    """ 课程类 """
    def __init__(self, c_number, c_name, teacher=None):
        """
        构造函数
        :param c_number: 课程编号
        :param c_name: 课程名称
        :param teacher: 授课教师，默认为空
        """
        self.c_number = c_number
        self.c_name = c_name
        self.teacher = teacher

    def binding(self, teacher):
        """ 实现课程绑定授课教师功能 """
        if teacher is None:
            return 0
        else:
            self.teacher = teacher
            return {'课程名称': self.c_name, "教师名称": teacher.t_name}
