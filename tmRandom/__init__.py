from flask import Flask
from .models.game import Game


app = Flask(__name__)

import tmRandom.views

