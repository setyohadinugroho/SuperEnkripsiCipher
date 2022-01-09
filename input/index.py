import flask
from flask import url_for

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
    message = ''
    if flask.request.method == 'POST':
        message = flask.request.form['name']
    return flask.render_template('index.html', message == message)

if __name__ == '__main__':
    app.run()