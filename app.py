from flask import Flask
from tasks import send

app = Flask(__name__)


@app.route("/")
def hello():
    # Producer for sending task to consumer
    send.apply_async(args=[4, 4], queue='send')
    return "Done !"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
