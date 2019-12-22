import logging.config

# class CustomManger(logging.Manager):
#     def getLogger(self, name):
#         logger = super(CustomManger, self).getLogger(name)
#         # 简单写一下，Formatter你自己实现吧
#         # formatter = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
#         filename = '{}.log'.format(name)
#         logger.addHandler(logging.FileHandler(filename))
#         logger.setLevel(logging.INFO)
#         # logger.setFormatter(formatter)
#         return logger
#
#
# manager = CustomManger(logging.root)

log_dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "access": {
            'level': 'DEBUG',
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": "access.log",
            "maxBytes": 1024*1024*5,
            "backupCount": 5,
            "encoding": "utf-8"
        },
        "boss": {
            'level': 'error',
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "boss.log",
            "maxBytes": 300,
            "backupCount": 5,
            "encoding": "utf8"
        }
    },
    "loggers": {
        "access": {
            "level": "INFO",
            "handlers": ["access"],
            "propagate": "no"
        },
        "boss": {
            "level": "INFO",
            "handlers": ["boss"],
            "propagate": "no"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"]
    }
}
def init_log():
    logging.config.dictConfig(log_dict)
