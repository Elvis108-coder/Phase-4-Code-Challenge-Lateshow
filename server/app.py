#!/usr/bin/env python3

from models import db, Episode, Guest, Appearance
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    response = [episode.to_dict() for episode in episodes]
    return make_response(jsonify(response), 200)

# GET /episodes/<id>
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.filter_by(id=id).first()
    if episode:
        return make_response(jsonify(episode.to_dict()), 200)
    else:
        return make_response(jsonify({"error": "Episode not found"}), 404)

# GET /appearances  ✅ This was missing!
@app.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    response = [appearance.to_dict() for appearance in appearances]
    return make_response(jsonify(response), 200)

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return make_response(jsonify(new_appearance.to_dict()), 201)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

# PATCH /appearances/<id>
@app.route('/appearances/<int:id>', methods=['PATCH'])
def update_appearance(id):
    appearance = Appearance.query.filter_by(id=id).first()
    if not appearance:
        return make_response(jsonify({"error": "Appearance not found"}), 404)
    data = request.get_json()
    try:
        if 'rating' in data:
            appearance.rating = data['rating']
        db.session.commit()
        return make_response(jsonify(appearance.to_dict()), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 400)

# DELETE /appearances/<id>
@app.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    appearance = Appearance.query.filter_by(id=id).first()
    if not appearance:
        return make_response(jsonify({"error": "Appearance not found"}), 404)
    db.session.delete(appearance)
    db.session.commit()
    return make_response('', 204)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
