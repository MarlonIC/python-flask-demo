from flask import Flask
from bikeway import bikeway
from coordinate_type import coordinate_type
from whereabouts import whereabouts

app = Flask(__name__)
app.register_blueprint(bikeway, url_prefix='/bikeway')
app.register_blueprint(coordinate_type, url_prefix='/coordinate_type')
app.register_blueprint(whereabouts, url_prefix='/whereabouts')

