SIZE = 4


def empty_maze():
    return [[0 for j in range(SIZE)] for i in range(SIZE)]


def is_safe(maze, x, y):
    print("here")
    if x >= 0 and x < SIZE and y >= 0 and y < SIZE and maze[x][y] == 1:
        print("here if")
        return True
    return False


def solve(maze):
    solution = empty_maze()
    if traverse_maze(maze, 0, 0, solution) == False:
        print("Solution doesnot exist")
        return False
    print("solution", solution)
    return True


def traverse_maze(maze, x, y, sol):
    if x == SIZE - 1 and y == SIZE - 1:
        sol[x][y] = 1
        return True
    if is_safe(maze, x, y) == True:

        sol[x][y] = 1
        if traverse_maze(maze, x + 1, y, sol) == True:
            return True
        if traverse_maze(maze, x, y + 1, sol) == True:
            return True

        sol[x][y] = 0
        return False


if __name__ == "__main__":
    maze = [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
    solve(maze)
