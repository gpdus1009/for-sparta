from flask import Flask, render_template, jsonify, request
# import requests
# from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.mbti  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

mbtiresult = [0,0,0,0,0,0,0,0]

@app.route('/')
def home():
    return render_template('mbti_test.html')


@app.route('/EI1', methods=["GET"])
def EI1():
    return render_template('EI1.html')

@app.route('/EI1', methods=['POST'])
def EI1_post():
    title_receive = request.form['title_give']
    if title_receive == "E":
        mbtiresult[0] = 1
        mbtiresult[1] = 0
    else :
        mbtiresult[0] = 0
        mbtiresult[1] = 1


    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/EI2')
def EI2():
    return render_template('EI2.html')

@app.route('/EI2', methods=['POST'])
def EI2_post():
    title_receive = request.form['title_give']
    if title_receive == "E":
        mbtiresult[0] += 1
    else:
        mbtiresult[1] += 1
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/EI3')
def EI3():
    return render_template('EI3.html')

@app.route('/EI3', methods=['POST'])
def EI3_post():
    title_receive = request.form['title_give']
    if title_receive == "E":
        mbtiresult[0] += 1
    else:
        mbtiresult[1] += 1

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/SN1')
def SN1():
    return render_template('SN1.html')

@app.route('/SN1', methods=['POST'])
def SN1_post():
    title_receive = request.form['title_give']
    if title_receive == "S":
        mbtiresult[2] = 1
        mbtiresult[3] = 0
    else :
        mbtiresult[2] = 0
        mbtiresult[3] = 1

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/SN2')
def SN2():
    return render_template('SN2.html')

@app.route('/SN2', methods=['POST'])
def SN2_post():
    title_receive = request.form['title_give']
    if title_receive == "S":
        mbtiresult[2] += 1
    else:
        mbtiresult[3] += 1

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/SN3')
def SN3():
    return render_template('SN3.html')

@app.route('/SN3', methods=['POST'])
def SN3_post():
    title_receive = request.form['title_give']
    if title_receive == "S":
        mbtiresult[2] += 1
    else:
        mbtiresult[3] += 1

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/TF1')
def TF1():
    return render_template('TF1.html')

@app.route('/TF1', methods=['POST'])
def TF1_post():
    title_receive = request.form['title_give']
    if title_receive == "T":
        mbtiresult[4] = 1
        mbtiresult[5] = 0
    else :
        mbtiresult[4] = 0
        mbtiresult[5] = 1

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/TF2')
def TF2():
    return render_template('TF2.html')

@app.route('/TF2', methods=['POST'])
def TF2_post():
    title_receive = request.form['title_give']
    if title_receive == "T":
        mbtiresult[4] += 1
    else:
        mbtiresult[5] += 1
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/TF3')
def TF3():
    return render_template('TF3.html')

@app.route('/TF3', methods=['POST'])
def TF3_post():
    title_receive = request.form['title_give']
    if title_receive == "T":
        mbtiresult[4] += 1
    else:
        mbtiresult[5] += 1
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/JP1')
def JP1():
    return render_template('JP1.html')

@app.route('/JP1', methods=['POST'])
def JP1_post():
    title_receive = request.form['title_give']
    if title_receive == "J":
        mbtiresult[6] = 1
        mbtiresult[7] = 0
    else :
        mbtiresult[6] = 0
        mbtiresult[7] = 1
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/JP2')
def JP2():
    return render_template('JP2.html')

@app.route('/JP2', methods=['POST'])
def JP2_post():
    title_receive = request.form['title_give']
    if title_receive == "J":
        mbtiresult[6] += 1
    else:
        mbtiresult[7] += 1
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

@app.route('/JP3')
def JP3():
    return render_template('JP3.html')

@app.route('/JP3', methods=['POST'])
def JP3_post():
    title_receive = request.form['title_give']
    if title_receive == "J":
        mbtiresult[6] += 1
    else:
        mbtiresult[7] += 1
    print(title_receive)
    print(mbtiresult)

    global mbtiresultstring
    mbtiresultstring = ""
    if mbtiresult[0] < mbtiresult[1] :
        mbtiresultstring += "I"
    else :
        mbtiresultstring += "E"

    if mbtiresult[2] < mbtiresult[3] :
        mbtiresultstring += "N"
    else :
        mbtiresultstring += "S"

    if mbtiresult[4] < mbtiresult[5] :
        mbtiresultstring += "F"
    else :
        mbtiresultstring += "T"

    if mbtiresult[6] < mbtiresult[7] :
        mbtiresultstring += "P"
    else :
        mbtiresultstring += "J"


    print(mbtiresultstring)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!', mbtiresultstring : mbtiresultstring})

@app.route('/showresult')
def showresult():
    return render_template('showresult.html')

@app.route('/showresult', methods= ['POST'])
def showresult_post():
    print(mbtiresult)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!','mbtiresultstring' : mbtiresultstring})



@app.route('/INFJ')
def INFJ():
    return render_template('INFJ.html')


@app.route('/INFP')
def INFP():
    return render_template('INFP.html')


@app.route('/INTJ')
def INTJ():
    return render_template('INTJ.html')


@app.route('/INTP')
def INTP():
    return render_template('INTP.html')


@app.route('/ISFJ')
def ISFJ():
    return render_template('ISFJ.html')


@app.route('/ISFP')
def ISFP():
    return render_template('ISFP.html')


@app.route('/ISTJ')
def ISTJ():
    return render_template('ISTJ.html')


@app.route('/ISTP')
def ISTP():
    return render_template('ISTP.html')


@app.route('/ENFJ')
def ENFJ():
    return render_template('ENFJ.html')


@app.route('/ENFP')
def ENFP():
    return render_template('ENFP.html')


@app.route('/ENTJ')
def ENTJ():
    return render_template('ENTJ.html')


@app.route('/ENTP')
def ENTP():
    return render_template('ENTP.html')


@app.route('/ESFJ')
def ESFJ():
    return render_template('ESFJ.html')


@app.route('/ESFP')
def ESFP():
    return render_template('ESFP.html')


@app.route('/ESTJ')
def ESTJ():
    return render_template('ESTJ.html')


@app.route('/ESTP')
def ESTP():
    return render_template('ESTP.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
