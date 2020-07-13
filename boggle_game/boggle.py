class Node:
    def __init__(self, *args, **kwargs):
        self.value = None
        self.left = None
        self.right = None
        self.top = None
        self.buttom = None
        self.top_left = None
        self.top_right = None
        self.buttom_left = None
        self.buttom_right = None


class BoardNode:
    def __init__(self, board_data, words):
        self.SIZE_X, self.SIZE_Y = len(board_data), len(board_data[0])
        self.full_board = [[0 for _ in range(self.SIZE_X)] for i in range(self.SIZE_X)]
        self.board = board_data
        self.words = words
        self.visited_words = []

    def build(self):
        for i in range(self.SIZE_X):
            for j in range(self.SIZE_Y):
                self.node = Node()
                r = j + 1
                l = j - 1
                t = i - 1
                b = i + 1

                if i == 0 and j == 0:
                    print("HERE")
                    self.node.value = self.board[i][j]
                    self.node.right = self.board[i][r]
                    self.node.buttom = self.board[b][j]
                    self.node.buttom_right = self.board[b][r]
                elif i == 0 and j == 3:
                    self.node.value = self.board[i][j]
                    self.node.left = self.board[i][l]
                    self.node.buttom = self.board[b][j]
                    self.node.buttom_left = self.board[b][l]
                elif i == 3 and j == 0:
                    self.node.value = self.board[i][j]
                    self.node.right = self.board[i][r]
                    self.node.top = self.board[t][j]
                    self.node.top_right = self.board[t][r]
                elif i == 3 and j == 3:
                    self.node.value = self.board[i][j]
                    self.node.left = self.board[i][l]
                    self.node.top = self.board[t][j]
                    self.node.top_left = self.board[t][l]
                elif i == 0:
                    self.node.value = self.board[i][j]
                    self.node.left = self.board[i][l]
                    self.node.right = self.board[i][r]
                    self.node.buttom = self.board[b][j]
                    self.node.buttom_left = self.board[b][l]
                    self.node.buttom_right = self.board[b][r]
                elif j == 0:
                    self.node.value = self.board[i][j]
                    self.node.right = self.board[i][r]
                    self.node.top = self.board[t][j]
                    self.node.buttom = self.board[b][j]
                    self.node.buttom_right = self.board[b][r]
                    self.node.top_right = self.board[t][r]
                elif i == 3:
                    self.node.value = self.board[i][j]
                    self.node.right = self.board[i][r]
                    self.node.left = self.board[i][l]
                    self.node.top = self.board[t][j]
                    self.node.top_right = self.board[t][r]
                    self.node.top_left = self.board[t][l]
                elif j == 3:
                    self.node.value = self.board[i][j]
                    self.node.left = self.board[i][l]
                    self.node.top = self.board[t][j]
                    self.node.top_left = self.board[t][l]
                    self.node.buttom_left = self.board[b][l]
                    self.node.buttom = self.board[b][j]
                else:
                    self.node.value = self.board[i][j]
                    self.node.left = self.board[i][l]
                    self.node.right = self.board[i][r]
                    self.node.top = self.board[t][j]
                    self.node.buttom = self.board[b][j]
                    self.node.top_left = self.board[t][l]
                    self.node.top_right = self.board[t][r]
                    self.node.buttom_left = self.board[b][l]
                    self.node.buttom_right = self.board[b][r]
                self.full_board[i][j] = self.node

    def is_valid_cell(self, node, char):
        return self.node.value == char

    def move_left(self, node):
        return self.node.left

    def move_right(self, node):
        return self.node.right

    def mode_top(self, node):
        return self.node.top

    def move_buttom(self, node):
        return self.node.buttom

    def move_top_left(self, node):
        return self.node.top_left

    def moove_top_right(self, node):
        return self.node.top_right

    def move_buttom_left(self, node):
        return self.node.buttom_left

    def move_buttom_right(self, node):
        return self.node.buttom_right

    def move(self, node, i, temp=""):
        if self.is_valid_cell(node, i):
            self.visited_node.append(node)
            temp += i
        else:
            self.visited_node.pop()
            self.move()

    def search(self, word):
        self.visited_node = []
        self.found = False
        temp = ""
        board = self.full_board
        if word in self.visited_words:
            return 0
        for i in word:
            if self.is_valid_cell(board, i):
                if temp == word:
                    self.visited_words.append(word)
                    return 1
                temp += i
        return -1

        for i in range(self.SIZE_X):
            for j in range(self.SIZE_Y):
                self.move(self.full_board[i][j])
                print(self.full_board[i][j].value)


if __name__ == "__main__":
    board_data = [
        ["x", "a", "i", "l"],
        ["m", "t", "x", "c"],
        ["e", "a", "i", "n"],
        ["t", "e", "p", "o"],
    ]
    word_record = ["max", "tax", "maxi", "taxi", "pet", "met", "meat"]
    board = BoardNode(board_data, word_record)
    board.build()
    board.search("fd")
    print("BOARD: ", [[i.value for i in row] for row in board.full_board])

