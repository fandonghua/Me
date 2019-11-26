import os
import time
from config.setting import projects_path


def clean_report(days=10):
    '''清理测试报告'''
    for cur_dir, dirs, files in os.walk(projects_path):#递归获取项目目录下所有文件夹
        if cur_dir.endswith('report'):#判断如果文件夹是report的话，获取文件夹下面的文件
            for report in files:
                if report.endswith('.html'):#如果是.html结尾的
                    report_path = os.path.join(cur_dir, report)
                    if os.path.getctime(report_path) < time.time() - 60 * 60 * 24 * days:
                        os.remove(report_path)
