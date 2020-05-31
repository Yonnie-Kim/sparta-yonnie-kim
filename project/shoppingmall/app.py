from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분


@app.route('/orders', methods=['POST'])
def make_order():
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    hpnum_receive = request.form['hpnum_give']

    order = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'hpnum': hpnum_receive
    }
    db.orders.insert_one(order)
    return jsonify({'result': 'success', 'msg': '접수 완료!'})


@app.route('/orders', methods=['GET'])
def read_order():
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
