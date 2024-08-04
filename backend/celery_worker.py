from celery import Celery
from flask import Flask
from config import Config

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app = Flask(__name__)
app.config.from_object(Config)
celery = make_celery(app)

@celery.task
def add(x, y):
    return x + y
