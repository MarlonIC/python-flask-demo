from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'hello world!'


@app.route('/name/<string:name>', methods=['GET'])
def get_name(name='Marlon'):
    return 'Hi ' + name


@app.route('/post/<int:id_post>', methods=['POST'])
def get_post(id_post):
    params = request.get_json()

    return jsonify({
        'id_post': id_post,
        'user': params.get('user')
    })
