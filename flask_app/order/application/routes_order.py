from flask import current_app as app
from flask import request, jsonify, abort
from werkzeug.exceptions import NotFound, BadRequest, UnsupportedMediaType, Unauthorized

from . import Session
from . import publisher_order
from .auth import RsaSingleton
from .model_order import Order

# Order Routes #########################################################################################################


@app.route('/order', methods=['POST'])
def create_order():
    session = Session()
    new_order = None
    if request.headers['Content-Type'] != 'application/json':
        abort(UnsupportedMediaType.code)
    content = request.json

    try:
        new_order = Order(
            description=content['description'],
            client_id=content['client_id'],
            number_of_pieces=content['number_of_pieces'],
            pieces_created=0,
            status=Order.STATUS_WAITING_FOR_PAYMENT
        )
        session.add(new_order)
        session.commit()

        datos = {"number_of_pieces": new_order.number_of_pieces,
                 "client_id": new_order.client_id,
                 "order_id": new_order.id}
        # publisher_order.publish_msg("event_exchange", "order.created", str(datos))
        print(datos)
    except KeyError:
        session.rollback()
        session.close()
        abort(BadRequest.code)
    response = jsonify(new_order.as_dict())
    session.close()
    return response

@app.route('/order', methods=['GET'])
@app.route('/orders', methods=['GET'])
def view_orders():
    session = Session()

    orders = session.query(Order).all()
    response = jsonify(Order.list_as_dict(orders))
    session.close()
    return response


@app.route('/order/<int:order_id>', methods=['GET'])
def view_order(order_id):
    session = Session()

    order = session.query(Order).get(order_id)
    if not order:
        abort(NotFound.code, "Given order id not found in the Database")
    response = jsonify(order.as_dict())
    session.close()
    return response


@app.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    session = Session()

    order = session.query(Order).get(order_id)
    if not order:
        abort(NotFound.code, "Order not found for given order id")
    publisher_order.publish_msg("event_exchange", "order.deleted", str(order.id))
    session.delete(order)
    session.commit()
    response = jsonify(order.as_dict())
    session.close()
    return response
