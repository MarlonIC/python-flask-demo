from flask import Blueprint
from models.repository.coordinate_type import CoordinateType
from models.provider.engine import session

coordinate_type = Blueprint('coordinate_type', __name__)


@coordinate_type.route('/', methods=['GET'])
def index():
    return 'hello world coordinate type!'


@coordinate_type.route('/<int:id_coordinate_type>', methods=['GET'])
def getCoordinateType(id_coordinate_type):
    coordinate_type_all = session.query(CoordinateType).all()
    print(coordinate_type_all)
    return 'hello world coordinate_type!'
