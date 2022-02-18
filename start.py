from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)
#CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/') 
#@cross_origin(origins='*')
def hello():
    return "Hello"

@app.route('/add', methods=['POST', 'GET'])
#@cross_origin(origins='*')
def add_caculation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return 'Ket qua la: ' + str(a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')