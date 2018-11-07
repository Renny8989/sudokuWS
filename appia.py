from flask import Flask
from flask import request, jsonify
from flask import make_response
from flask import abort
import numpy as np

app = Flask(__name__)

Sudoku = np.array([[7,0,0,0,4,0,5,3,0],[0,0,5,0,0,8,0,1,0], [0,0,8,5,0,9,0,4,0],
                   [5,3,9,0,6,0,0,0,1],[0,0,0,0,1,0,0,0,5], [8,0,0,7,2,0,9,0,0],
                   [9,0,7,4,0,0,0,0,0],[0,0,0,0,5,7,0,0,0], [6,0,0,0,0,0,0,5,0] ])

def checkMove(n,r,c):
    global Sudoku
    if 1 <= n <= 9 and 1 <= r <= 9 and 1 <= c <= 9:
        if Sudoku[r-1,c-1] == 0:
            if n not in Sudoku[r-1] and n not in Sudoku[:,c-1]:
                return True


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/sudoku', methods=['GET'])
def index():
    return jsonify({'Sudoku':Sudoku.tolist()})


@app.route('/sudoku/move', methods=['POST'])
def insert():
    if not request.json or not 'n' in request.json:
        abort(400)
    n = request.json['n']
    r = request.json['r']
    c = request.json['c']
    global Sudoku
    if checkMove(n,r,c) == True:
        Sudoku[r-1,c-1]= n
    else:
        abort(400)
    return jsonify({'Sudoku':Sudoku.tolist()})


if __name__=='__main__':
    app.run(debug=True)