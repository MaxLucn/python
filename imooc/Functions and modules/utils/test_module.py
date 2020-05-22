from datetime import datetime

from trans.tools import gen_trans_id

from trans import tools as trans_tools
import work


def test_trans_tool():
    """测试 trans 包下的 tools 模块"""
    id1 = trans_tools.gen_trans_id()
    print(id1)
    date = datetime(2015, 10, 2, 12, 30, 35)
    id2 = trans_tools.gen_trans_id(date)
    print(id2)


def test_work_tool():
    """测试 work 模块"""
    file_name = '/Users/luweilei/Pictures/psb.doc'
    rest = work.tools.get_file_type(file_name)
    print(rest)


if __name__ == "__main__":
    test_trans_tool()
    test_work_tool()
