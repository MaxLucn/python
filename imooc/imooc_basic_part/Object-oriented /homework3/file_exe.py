from example import Course,  Teacher, Student


def introduction(str):
    """ 输出标题 """
    print("*********{}*********".format(str))


def prepare_course():
    """
    创建课程信息初始化，并以列表形式返回所创建的 8 门课程
    """
    my_dict = {'01': '网络爬虫', '02': '数据分析', '03': '人工智能', '04': '机器学习',
               '05': '云计算', '06': '大数据', '07': '图像识别', '08': 'Web开发'}
    # 创建课程实例列表
    my_list = []
    for k, v in my_dict.items():
        course = Course(k, v)
        my_list.append(course)
    return my_list


def create_teacher():
    """ 创建教师信息初始化，并以列表形式返回所创建的 8 名教师对象 """
    my_list1 = []
    list_info = [['T1', '张亮', '13301122001'], ['T2', '王朋', '13301122002'], ["T3", "李旭", "13301122003"],
                 ["T4", "黄国发", "13301122004"], ["T5", "周勤", "13301122005"], ["T6", "谢富顺", "13301122006"],
                 ["T7", "贾教师", "13301122007"], ["T8", "杨教师", "13301122008"]]
    for i in list_info:
        teacher = Teacher(i[0], i[1], i[2])
        my_list1.append(teacher)
    return my_list1


def course_to_teacher():
    """实现课程与教师逐一绑定（每一课程信息绑定倒叙的每一老师信息），并以列表形式返回所课程与教师的绑定结果"""
    my_list2 = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for i in range(0, len(ls_course)):
        my_list2.append(ls_course[i].binding(ls_teacher[-(i + 1)]))
    return my_list2


def create_student():
    """创建学生信息初始化，并以列表形式返回所创建的8名学生对象"""
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    my_list3 = []
    list_number = range(1000, 1008)
    for i in range(len(list_number)):
        student = Student( ls_student[-(i+1)], list_number[i])
        my_list3.append(student)
    return my_list3


if __name__ == "__main__":
    my_list2 = course_to_teacher()
    my_list3 = create_student()
    introduction("慕课学院(1)班学生信息")
    for i in my_list3:
        i.__str__()
    introduction("慕课学院(1)班选课结果")
    for i in range(len(my_list3)):
        my_list3[i].add_course(my_list2[i])
    for i in my_list3:
        print('Name:{0}, Selected: {1}'.format(i.name, i.course_detail))