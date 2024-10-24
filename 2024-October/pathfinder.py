import time


class Pathfinder:
    def __init__(self, start, goal, possible_paths_trie):
        self.board = [
            ['a', 'a', 'a', 'b', 'b', 'c'],
            ['a', 'a', 'a', 'b', 'b', 'c'],
            ['a', 'a', 'b', 'b', 'c', 'c'],
            ['a', 'a', 'b', 'b', 'c', 'c'],
            ['a', 'b', 'b', 'c', 'c', 'c'],
            ['a', 'b', 'b', 'c', 'c', 'c'],
        ]
        self.n = len(self.board)
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        self.start = start
        self.goal = goal
        self.all_paths = []  # To store all valid paths
        self.trie = possible_paths_trie

    def dfs(self, path, tiles):
        # Get the current point in the path
        current_point = path[-1]

        # Check if we've reached the goal
        if current_point == self.goal and tiles in self.trie:
            self.all_paths.append(beautiful_print(path))
            return

        # Recursively explore each move
        for move in self.moves:

            new_x = current_point[0] + move[0]
            new_y = current_point[1] + move[1]

            if new_x < 0 or new_y < 0 or new_x >= self.n or new_y >= self.n:
                continue

            new_point = (new_x, new_y)
            next_tile = self.board[new_y][new_x]

            new_tiles = f"{tiles}{next_tile}"

            if new_point not in path and len(self.trie.keys(new_tiles)) > 0:
                path.append(new_point)  # Add the move to the current path

                self.dfs(path, new_tiles)  # Recursively call dfs with the new path

                path.pop()  # Backtrack after exploring this path


    def find_all_paths(self):
        self.dfs([self.start], 'a')  # Start DFS from the initial point
        return self.all_paths


def beautiful_print(path):
    # Map for x-axis (0-5 to 'a'-'f')
    x_map = ['a', 'b', 'c', 'd', 'e', 'f']

    # Transform each (x, y) to chess-like format
    chess_path = [f"{x_map[x]}{y + 1}" for x, y in path]

    return chess_path