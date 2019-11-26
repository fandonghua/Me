import sys, os

base_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base_path)
from utils.project import Project
from utils import clean


def create_project():
    name = input('请输入项目名称：').strip()
    if not name:
        print('请输入项目名称！')
        return
    project = Project(name)
    project.main()

    print('【%s】project create success!' % name)


def clean_report():
    days = input('请输入清理几天的日志，默认清理10天：').strip()
    if days.isdigit():
        clean.clean_report(int(days))
    elif days == '':
        clean.clean_report()
    else:
        print('天数输入不合法！')


def main():
    func_map = {'1': create_project, '2': clean_report}
    msg = '''
    1 => 创建项目
    2 => 清理报告
    other => 退出
    >>>:'''
    choice = input(msg).strip()
    if choice in func_map:
        func_map[choice]()
    else:
        print('退出')


if __name__ == '__main__':
    main()
