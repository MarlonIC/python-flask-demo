from flask import Blueprint
from models.repository.bikeway import Bikeway
from models.provider.engine import session


bikeway = Blueprint('bikeway', __name__)


@bikeway.route('/', methods=['GET'])
def index():
    return 'hello world bikeway!'


@bikeway.route('/<int:id_bikeway>', methods=['GET'])
def getBikeway(id_bikeway):
    bikeway = session.query(Bikeway).filter_by(id_bikeway=id_bikeway).first()
    print(bikeway.characteristic)
    return 'hello world bikeway!'
