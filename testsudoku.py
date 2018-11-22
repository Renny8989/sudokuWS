import unittest
# in larger project you store them in different folders and use python path so that the test code can import the production code
import sudoku
from sudoku import isFinished
from sudoku import insert
from sudoku import Sudoku
from sudoku import checkMove
#from werkzeug.exceptions import HTTPException
import numpy as np

class Sudokutest(unittest.TestCase):

    def test_isFinished_base(self):
        self.assertEqual(isFinished(Sudoku), False)


    def test_isFinished_intermediate(self):
        self.assertEqual(isFinished(np.array([[7,0,0,0,4,0,5,3,0],[0,0,5,0,0,8,0,1,0], [0,0,8,5,0,9,0,4,0],
                   [5,3,9,0,6,0,0,0,1],[0,0,0,0,1,0,0,0,5], [8,0,0,7,2,0,9,0,0],
                   [9,0,7,4,0,0,0,0,0],[0,0,0,0,5,7,0,0,0], [6,0,0,0,0,0,0,5,0] ])), False)


    def test_isFinished_End(self):
        self.assertEqual(isFinished(np.array([[7, 9, 9, 9, 4, 9, 5, 3, 9], [1, 1, 5, 1, 3, 8, 4, 1, 8], [1, 1, 5, 1, 3, 8, 4, 1, 8],
                                 [5, 3, 9, 2, 6, 2, 2, 2, 1], [1, 1, 5, 1, 3, 8, 4, 1, 8], [1, 1, 5, 1, 3, 8, 4, 1, 8],
                                 [1, 1, 5, 1, 3, 8, 4, 1, 8], [1, 1, 5, 1, 3, 8, 4, 1, 8],
                                 [1, 1, 5, 1, 3, 8, 4, 1, 8]])), True)

    ###### BELOW INTEGRATION TEST! REQUIRES CONTEXT! HTTP REQUEST! #####
    ####
    #def test_insert_CheckMoveNotTrue(self):
        # ensure that if check move is not true a 400 error will be returned
        #checkMove(10,1,1)
        #with self.assertRaises(HTTPException) as http_error:
         #   insert()
            #self.assertEqual(http_error.exception.code, 400)

    def test_checkMove(self):
        self.assertEqual(checkMove(6,6,6),False)

    def test_checkMove_2(self):
        self.assertEqual(checkMove(6,7,2),False)

    def test_checkMove_3(self):
        self.assertEqual(checkMove(611,7,2),False)

    def test_checkMove_ok(self):
        self.assertEqual(checkMove(4,5,1),True)

    def test_checkMove_column(self):
        self.assertEqual(checkMove(7,5,1),False)








