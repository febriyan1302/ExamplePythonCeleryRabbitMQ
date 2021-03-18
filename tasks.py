from celery import Celery

app = Celery('tasks', broker='amqp://guest@rabbitmq:5672')


@app.task
def send(x, y):
    return x + y

