from flask import Flask, jsonify, request
import database

app = Flask(__name__)
database.create_table()

@app.route('/')
def start():
    return jsonify({"server":"ok"})

@app.route('/device', methods=['GET','POST'])
def device():
    if request.method == 'POST':
        data = request.json
        database.insert_table(data['device'],data['temperature'],data['humidity'])
        return jsonify({"response":"ok"})

    elif request.method == 'GET':
        return jsonify({"server":"ok"})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")