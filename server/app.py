#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Bakery GET-POST-PATCH-DELETE API</h1>'

@app.route('/bakeries')
def get_all_bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    return jsonify(bakeries)

@app.route('/bakeries/<int:id>')
def get_bakery_by_id(id):
    bakery = Bakery.query.get_or_404(id)
    return jsonify(bakery.to_dict())

@app.route('/baked_goods/by_price')
def get_baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    baked_goods_serialized = [bg.to_dict() for bg in baked_goods]
    return jsonify(baked_goods_serialized)

@app.route('/baked_goods/most_expensive')
def get_most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first_or_404()
    return jsonify(most_expensive.to_dict())

if __name__ == '__main__':
    app.run(port=5555, debug=True)
