from flask import render_template, request
from tmRandom import app
from .models.game import Game
import json


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get('merchantsExpansion') == 'on':
            merchants = True
        else:
            merchants = False
        if request.form.get('miniExpansion') == 'on':
            mini = True
        else:
            mini = False
        num_players = request.form['numPlayers']
        players = [request.form['Player1'], request.form['Player2'], request.form['Player3'], request.form['Player4'],
                   request.form['Player5']]
        new_game = Game(merchants=merchants, mini=mini, num_players=num_players, players=players)

        return game(new_game.output())
    else:
        return render_template("main.html")

    
@app.route('/game', methods=["GET", "POST"])
def game(game_json):
    if 'restart' in request.method:
        return render_template("main.html")
    elif 'faction' in request.method:
        pass
    else:
        json.loads(game_json)
        return render_template('game.html', game_dict=json.loads(game_json))

