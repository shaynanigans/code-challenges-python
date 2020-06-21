import copy

# This object stores the Boggle Grid in graph form for easier traversal
class Graph(object):
    def __init__(self, board):
        self.board = board
        # Mapof Letter:[Co-ordinates] key-value pairs
        self.letter_coordinates = {}
        # Map containing list of adjacent letters for each letter in grid
        self.adjacent_letters = {}
        # Map of steps we can take in each direction from a given letter
        # directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        length = len(board)
        width = len(board[0])
        for i in range(length):
            for j in range(width):
                # TODO validate for non-English letters, not just numbers.
                # Tidy handling of exception
                if not board[i][j].isalpha():
                    raise Exception("Invalid letter supplied: ", board[i][j])
                # If letter on board not in co-ordinates map, create entry
                if board[i][j] not in self.letter_coordinates:
                    self.letter_coordinates[board[i][j]] = []
                # Add coordinates to map
                self.letter_coordinates[board[i][j]].append((i, j))
                # Find all letters adjacent to this letter and add them to map
                self.adjacent_letters[(board[i][j], i, j)] = []
                for dir_1, dir_2 in directions:
                    k = i+dir_1
                    l = j+dir_2
                    if k >= 0 and k < length and l >= 0 and l < width:
                        self.adjacent_letters[(board[i][j], i, j)].append((board[k][l], k, l))


    def dfs(self, word):
        # If the word is length zero or longer than 10^3, return false
        if len(word) == 0:
            return False
        if len(word) > 10^3:
            return False

        stack = []
        # If the first letter of the word is not 
        if word[0] not in self.letter_coordinates:
            return False

        # Push first letter address on stack
        for i, j in self.letter_coordinates[word[0]]:
            stack.append((word[0], word, (word[0], i, j), set([(i, j)])))

        while len(stack) > 0:
            # Decompose the item at top of stage into its separate attributes
            substring, word, letter, positions = stack.pop()

            if substring == word:
                # If we have found the word, return True
                return True

            next_letter = word[len(substring)]
            for let, i, j in self.adjacent_letters[letter]:
                # If this index isn't already in our stack, and the letter is next in the word, add it to the stack.
                if (i, j) not in positions and let == next_letter:
                    updated_positions = copy.deepcopy(positions)
                    updated_positions.add((i, j))
                    stack.append((substring + next_letter, word, (let, i, j), updated_positions))
        return False

class Boggle_Puzzle: 
    def __init__(self, board):
        self.board = board
        self.boggle_graph = Graph(board)

    def is_word_valid(self,word):
        return True

    def find_word(self, word):
        if self.boggle_graph.dfs(word):
            return True
        return False

# Main method, validating method against data/example in problem sheet
if __name__ == '__main__': 
    sample_board=[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    puzzle = Boggle_Puzzle(sample_board)

    print("Grid contains word 'ABCB':", puzzle.find_word('ABCB'))
    print("Grid contains word 'ABCCED':", puzzle.find_word('ABCCED'))
    print("Grid contains word 'SEE':", puzzle.find_word('SEE'))

