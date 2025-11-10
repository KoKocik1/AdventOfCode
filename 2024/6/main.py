from classes import Board, Player, Position, Bot, VisitedStates, VisitedState
from pathlib import Path
from helpers import GetFile
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
        bot = Bot()
        bot.set_start_point(player.get_position())

        test_board = board.deep_copy()
        test_board.set_character_at_position(
            visited_state.position.row, visited_state.position.col, '#')
        has_loop = bot.test_loop(test_board, player)
        if has_loop:
            found_obstacles.add_visited_state(visited_state)
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
