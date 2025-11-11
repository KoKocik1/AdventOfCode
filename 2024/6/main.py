from classes import Player, LoopChecker, VisitedStates, VisitedState
from pathlib import Path
from helpers import GetFile, Board, Position
from tqdm import tqdm


def part1(board: Board, player: Player):
    visited = VisitedStates()
    while True:
        if not player.move(board):
            break
        visited.add_visited_state(VisitedState(
            player.get_position()))
    print(f"Total X: {board.count_characters('X')}")
    return visited


def part2(board: Board, player: Player, visited: VisitedStates):
    found_obstacles = VisitedStates()

    for visited_state in tqdm(visited.visited_states, desc="Checking obstacles"):
        if visited_state.position == player.get_position():
            continue
        loop_checker = LoopChecker(player.get_position())

        r = visited_state.position.row
        c = visited_state.position.col
        position = Position(r, c)

        old_character = board.get_character(position)
        board.set_character_at_position(position, '#')
        has_loop = loop_checker.test_loop(board, player)
        if has_loop:
            found_obstacles.add_visited_state(visited_state)
        board.set_character_at_position(position, old_character)
    print(f"Total obstacles: {len(found_obstacles.visited_states)}")


def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file_reader = GetFile(data_file, '')
    board = Board(file_reader.get_2d_array())
    start_position = board.find_character_position('^')
    player = Player(start_position)
    visited = part1(board, player)
    player = Player(start_position)
    part2(board, player, visited)


if __name__ == "__main__":
    main()
