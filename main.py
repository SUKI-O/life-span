"""
main class for life span

"""
from flask import Flask, render_template

app = Flask(__name__)

from user import *
from counter import *
from display import *


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    name = 'Life Span'
    return render_template('index.html', title=name)

if __name__=="__main__":
    app.run()


class main:
    def __init__(self):
        user = User()
        couter = Counter()
        display = Display()