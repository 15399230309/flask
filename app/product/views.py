import logging
# from log import manager
from flask import (
    Blueprint
)
bp = Blueprint('auth', __name__, url_prefix='/product')
logger_product = logging.getLogger('access')
from app.emali import send_mail
@bp.route('/log',methods=['GET'])
def make_log():

    logger_product.info('i`m in product')
    logger_product.error('i`m in product')
    logger_product.debug('i`m in product')
    return 'success'

@bp.route('/mail',methods=['GET'])
def make_mail():
    subject = '这是一个测试邮件'
    recipients= ['xxxx@163.com']
    body = '我是一个兵，来自老板姓'
    html='<h1>滴答答嘟嘟哒哒，葫芦娃</h1>'
    cc=['xxxx@qq.com']
    send_mail(subject,recipients,body,html,cc)
    return body
