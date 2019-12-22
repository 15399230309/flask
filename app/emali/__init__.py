from run import mail
from flask_mail import Message


def send_mail(subject,recipients,body,html,cc):
    try:
        msg = Message(subject=subject,
                      recipients=recipients,
                      body=body,
                      html=html,
                      cc=cc,
                      )
        mail.send(msg)
    except Exception as e:
        print( '发送邮件失败，is %s' % e)
        raise (e)