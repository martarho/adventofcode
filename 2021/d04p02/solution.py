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
    winners = []
    winners_index = []
    for d,b in enumerate(boards):
        if n in b.board_matrix:
            xy = np.where(b.board_matrix == n)
            b.add_match(xy)
            evl = b.check_matrix()
            if evl == 1:
                winners.append((b,n))
                winners_index.append(d)
                # remove winner board from the list
    for wi in sorted(winners_index, reverse=True):
        _ = boards.pop(wi)
    return (winners, boards)



if __name__ == "__main__":
    numbers, boards = load_file("../data/day04_input.txt")

    winners_list = []
    for n in numbers:
        # Check all boards
        winners, boards = evaluate_boards(n, boards)
        winners_list.extend(winners)

    # Sanity check - first problem
    winner_board, winner_number = winners_list[0]
    winner_board.calculate_score(winner_number)

    # second problem
    winner_board, winner_number = winners_list[-1]
    winner_board.calculate_score(winner_number)
