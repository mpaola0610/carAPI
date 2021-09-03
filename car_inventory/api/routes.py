import re
from flask import Blueprint, json, request, jsonify
from werkzeug.wrappers import response
from car_inventory.helpers import token_required
from car_inventory.models import db, User, Car, car_schema, cars_schema


api = Blueprint('api', name, url_prefix = '/api')

@api.route('/getdata')
@token_required
def get_data(current_user_token):
    return { 'some' : 'value' }

# CREATE CAR ENDPOINT
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    camera_quality = request.json['camera_quality']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_product = request.json['cost_of_product']
    series = request.json['series']
    user_token = current_user_token.token

    car = Car(name,description,price,camera_quality,flight_time, max_speed, dimensions, weight, cost_of_product, series, user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

#UPDATE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['Post', 'PUT'])
@token_required
def update_drone(current_user_token, id):
    drone = Car.query.get(id) # Get car Instance

    car.name = request.json['name']
    car.description = request.json['description']
    car.price = request.json['price']
    car.camera_quality = request.json['camera_quality']
    car.flight_time = request.json['flight_time']
    car.max_speed = request.json['max_speed']
    car.dimensions = request.json['dimensions']
    car.weight = request.json['weight']
    car.cost_of_product = request.json['cost_of_product']
    car.series = request.json['series']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# DELETE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_drone(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)