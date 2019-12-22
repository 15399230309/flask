from flask import Flask
from config import  init_mail
from log import init_log
from app.product.views import bp
app = Flask(__name__)
mail = init_mail(app)
init_log()
app.register_blueprint(bp)


if __name__ == '__main__':
    app.run(debug=True)