from flask_mail import Mail, Message


def init_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.qq.com'
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'xxx@qq.com'
    app.config['MAIL_PASSWORD'] = 'xxx'
    app.config['MAIL_DEFAULT_SENDER'] = 'xxx'
    mail = Mail(app)
    return   mail