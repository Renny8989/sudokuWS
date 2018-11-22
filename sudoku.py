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
                rs = r % 3
                cs = c % 3
                if r % 3 == 0:
                    rs = 3
                if c % 3 == 0:
                    cs = 3
                if n not in Sudoku[r - rs:r - rs + 3, c - cs:c - cs + 3]:
                    return True
    return False


def isFinished(sudoku):
    if 0 in sudoku:
        return False
    else:
        return True


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#@app.errorhandler(Exception)
#def not_found(error):
#    return make_response(jsonify({'error': error}), 400)

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
        #raise Exception("mossa non valida")
    if isFinished(Sudoku):
        return jsonify({'Sudoku Completed': Sudoku.tolist()})
    else:
        return jsonify({'Sudoku':Sudoku.tolist()})


if __name__=='__main__':
    app.run(debug=True)