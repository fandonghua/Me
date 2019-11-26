import unittest
import datetime
import os
import nnreport
from projects.litemall.public.const import case_path, report_path
from config.setting import email_template
from utils.send_message import send_mail


def run():
    test_suite = unittest.defaultTestLoader.discover(case_path, 'test*.py')
    # 这里是指定找什么开头的.py文件，运行用例的时候可以自己改
    report = nnreport.BeautifulReport(test_suite)
    title = 'litemall_测试报告'
    filename = title + '_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.html'
    report.report(description=title,
                  filename=filename,
                  log_path=report_path)
    email_content = email_template.format(pass_count=report.success_count,
                                          fail_count=report.failure_count,
                                          all_count=report.success_count + report.failure_count)

    report_abs_path = os.path.join(report_path, filename)
    send_mail(filename, email_content, report_abs_path)


if __name__ == '__main__':
    run()
