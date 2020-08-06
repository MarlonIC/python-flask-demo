from flask import Flask, request, jsonify
from whereabouts import whereabouts

app = Flask(__name__)
app.register_blueprint(whereabouts, url_prefix='/whereabouts')

