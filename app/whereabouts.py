from flask import Blueprint, request, jsonify

whereabouts = Blueprint('whereabouts', __name__)


@whereabouts.route('/', methods=['GET'])
def index():
    return 'hello world whereabouts!'


@whereabouts.route('/<int:id_whereabouts>', methods=['POST'])
def get_whereabouts(id_whereabouts):
    params = request.get_json()
    print(params)

    return jsonify({
        'id_whereabouts': id_whereabouts,
    })
