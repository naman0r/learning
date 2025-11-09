# amazon question
# array question in neetcode roadmap
#https://leetcode.com/problems/valid-sudoku/description/


# this problem is lowkey from hell.......

# check each 3x3 grid, check each column and row. 
# each number has to be between 1-9 
# unique rows, columns and 3x3 grids
# set? hashset? 

import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # unique hashset for every single row
        # row is in the x axis, column is in the y axis....

        '''
        tc of rows = 0(1) for each row = o(1)
        tc of cols = 0(1) for each row = o(1)
        tc of 3x3 grids = o(9^2) = o(1)

        hence time complexity (in theory) should be o(1) I THINK
        '''

        ''' 
        order of 3x3 grids
        0 1 2
        1
        2


.

        0 1 2 3 4 5 6 7 8 
        1
        2
        3
        4
        5
        6
        7
        8

        '''

        # fancy way to make a set
        cols = collections.defaultdict(set) # key: col num, value: set of nums in that column. 
        rows = collections.defaultdict(set) # same for rows
        squares = collections.defaultdict(set) # key = (r/3, c/3) (tuple)


        for r in range(9): 
            for c in range (9): 
                # check if it is empty, if so then skip
                if board[r][c] == ".": 
                    continue
                
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]): 
                    return False # duplicate

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                print(rows)
                squares[(r//3, c//3)].add(board[r][c])
                
        return True









        


        