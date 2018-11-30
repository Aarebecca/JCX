from flask import Flask, jsonify, make_response, request
from app import utils
import json
import os


jcx = Flask(__name__, static_url_path=json.load(open(os.path.dirname(__file__)+'/../asset/config.json', 'r'),
                                                encoding='UTF-8')["staticbase"])



