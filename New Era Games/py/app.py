from flask import Flask, render_template, jsonify
from models import db, Game

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://girbau:girbau123@localhost/new-era-games'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)



@app.route('/')
def games_page():
    return render_template('games.html')

@app.route('/api/games')
def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])

@app.route('/api/games/<category>')
def get_games_by_category(category):
    if category == 'all':
        games = Game.query.all()
    else:
        games = Game.query.filter_by(category=category).all()
    return jsonify([game.to_dict() for game in games])