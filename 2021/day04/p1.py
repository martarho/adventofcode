from dataclasses import dataclass 
import numpy as np 

def load_matrix(bl):
    arr = np.array(bl)
    b = Board(arr,
                np.zeros((5,5))
        )
    return b

def load_file(filename):
    drawn_numbers = []
    boards = []
    board = []
    for line in open(filename, 'r'):
        if ',' in line:
            # first line
            drawn_numbers = [int(i) for i in line.rstrip().split(",")]
        elif line == "\n":
            # new board
            if board != []:
                b = load_matrix(board)
                boards.append(b)
            board = []
        else:
            # Board lines
            values = [ int(i) for i in line.rstrip().lstrip().split(" ") if i != '']
            board.append(values)
    b = load_matrix(board)
    boards.append(b)
    return drawn_numbers, boards


@dataclass
class Board:
    board_matrix: np.ndarray
    board_matches: np.ndarray
    
    def add_match(self,coords):
        self.board_matches[coords] = 1

    def check_matrix(self):
        row_sums = self.board_matches.sum(axis=(0))
        col_sums = self.board_matches.sum(axis=(1))
        if (5 in row_sums) or (5 in col_sums):
            return 1
        return 0

    def calculate_score(self, n):
        coordinates_zeroes = np.where(self.board_matches == 0)
        score_values = self.board_matrix[coordinates_zeroes]
        board_score = score_values.sum()
        final_score = n*board_score
        print("Board Score %d\n Winner number %d\n FINAL SCORE: %d" % (board_score, n, final_score))


    

def evaluate_boards(n, boards):
    for d,b in enumerate(boards):
        print("Board %d" % (d))
        if n in b.board_matrix:
            xy = np.where(b.board_matrix == n)
            b.add_match(xy)
            evl = b.check_matrix()
            print("Evaluation %d" % (evl))
            if evl == 1:
                return (b, n, boards)
    return (None, None, boards)


if __name__ == "__main__":
    numbers, boards = load_file("../data/day04_input.txt")

    print("Board length %d" % (len(boards)))
    for n in numbers:
        # Check all boards
        print("value %d" % (n))
        winner_board, winner_number, boards = evaluate_boards(n, boards)
        if winner_number is not None:
            print("Bingo!")
            break

    print(winner_board)
    winner_board.calculate_score(winner_number)