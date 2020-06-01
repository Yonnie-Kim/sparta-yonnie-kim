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
def write_orders():
    # 클라이언트가 준 name, amount, address, phonenumber 값 받아오기
    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']

    # DB에 삽입할 order 만들기
    order = {
        'name': name_receive,
        'amount': amount_receive,
        'address': address_receive,
        'phonenumber': phonenumber_receive
    }

    # orders DB에 주문내용 저장하기
    db.orders.insert_one(order)
    # 처리 성공 시 성공메세지 반환하기
    return jsonify({'result': 'success', 'msg': '주문이 접수되었습니다.'})


@app.route('/orders', methods=['GET'])
def read_orders():
    # 요고 DB에서 리뷰정보 가져오는 것까지 완료해야 주소/orders에 API 리스트가 제대로 뜬다!
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
