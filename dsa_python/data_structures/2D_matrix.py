"""
    2D Matrices can be used to store a graph or a grid where nodes are added.
    For example, we could have a network of bouys in the ocean, or sensors in a swarm, 
    or a maze represented using a 2D structure.
"""
from typing import Tuple, List, Text


class Maze:
    OBSTACLE = '*'
    OPEN_SPACE = ' '

    def __init__(self, shape=None, maze_file_path=None) -> None:
        if maze_file_path:
            self.grid = self.load_maze_from_file(maze_file_path)
            self.shape = (len(self.grid), len(self.grid[0]))
        else:
            if not shape:
                raise ValueError(
                    "Neither Maze file, nor shape specified for maze. Please provide either one.")
            self.grid = self.create_empty_grid(shape)
            self.shape = (len(self.grid), len(self.grid[0]))

    def create_empty_grid(self, shape: Tuple) -> List[List[Text]]:
        grid = [['' for _ in range(shape[1])] for _ in range(shape[0])]
        return grid

    def load_maze_from_file(self, maze_file_path):
        try:
            content = ''
            with open(maze_file_path, 'r') as f:
                content = f.read()
            lines = content.split('\n')
            grid = []
            for line in lines:
                grid.append(list(line))
            n_top_row_cols = len(grid[0])
            for row in grid:
                if len(row) != n_top_row_cols:
                    print("Maze is not rectangular!")
                    raise SystemExit
            return grid
        except OSError:
            print("There's a problem with the file you have selected!")
            raise SystemExit

    def find_open_neighbours(self, i, j):
        "neighbours will be returned in the order of north, east, south, west."
        open_neighbors = []
        if i >= 1:
            n = self.grid[i - 1][j]
            if n != self.OBSTACLE:
                open_neighbors.append((i-1, j))
        if j < self.shape[1] - 1:
            e = self.grid[i][j + 1]
            if e != self.OBSTACLE:
                open_neighbors.append((i, j + 1))
        if i < self.shape[0] - 1:
            s = self.grid[i + 1][j]
            if s != self.OBSTACLE:
                open_neighbors.append((i+1, j))
        if j >= 1:
            w = self.grid[i][j - 1]
            if w != self.OBSTACLE:
                open_neighbors.append((i, j - 1))
        return open_neighbors


if __name__ == '__main__':
    # maze = Maze(maze_file_path='../data/mazes/diagonal_maze.txt')
    maze = Maze(maze_file_path='dsa_python/data/mazes/diagonal_maze.txt')
    for row in maze.grid:
        print(row)
    print(maze.find_open_neighbours(1,2))
