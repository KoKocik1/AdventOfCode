from pathlib import Path

from helpers import GetFile
from helpers.array_helper import Position, Board
from _2024._18.classes import PathFinder


def part1(points: list[Position], size_x: int, size_y: int, obstacles_size: int) -> int:
    board = load_board(points, size_x, size_y, obstacles_size)
    path_finder = PathFinder(board)
    
    shortest_path = path_finder.find_shortest_path()
    #path_finder.draw_path()
    return shortest_path


def part2(points: list[Position], size_x: int, size_y: int, obstacles_size: int) -> int:
    
    board = load_board(points, size_x, size_y, obstacles_size)
    path_finder = PathFinder(board)
        
    while True:
        obstacles_size += 1
        path_finder.add_new_obstacle(points[obstacles_size])
        shortest_path = path_finder.find_shortest_path()
        #path_finder.draw_path()
        if shortest_path is None:
            return points[obstacles_size], obstacles_size

def load_board(points: list[Position], size_x: int, size_y: int, obstacles_size: int) -> Board:
    board = []
    points_set = set(points[:obstacles_size])
    for x in range(size_x):
        row = []
        for y in range(size_y):
            row.append('#' if Position(x, y) in points_set else '.')
        board.append(row)
    return Board(board)

def load_points(file: GetFile) -> list[Position]:
    points = []
    for row in file.get_row():
        points.append(Position(int(row[1]), int(row[0])))
    return points

def main():
    data_file = Path(__file__).parent / 'data/test.txt'
    file = GetFile(str(data_file), delimiter=',')
    points = load_points(file)
    
    board_x_size = 7
    board_y_size = 7
    obstacles_size = 12
    print(part1(points, board_x_size, board_y_size, obstacles_size))
    print(part2(points, board_x_size, board_y_size, obstacles_size))


if __name__ == "__main__":
    main()
