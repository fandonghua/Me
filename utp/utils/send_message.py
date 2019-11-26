import yamail
import traceback
from config.setting import email_info, email_cc, email_to, log


def send_mail(subject, content, files=None):
    '''
    发送邮件
    :param subject:主题
    :param content: 内容
    :param files: 附件
    :return:
    '''
    try:
        smtp = yamail.SMTP(**email_info)
        smtp.send(subject=subject, contents=content,
                  to=email_to, cc=email_cc, attachments=files)
    except Exception as e:
        log.error("发送邮件失败+%s" % traceback.format_exc())


def send_sms():
    '''
    发送短信验证码
    :return:
    '''
    pass
