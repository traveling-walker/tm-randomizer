from flask import Flask
from .game import Game


app = Flask(__name__)

import tmRandom.views

