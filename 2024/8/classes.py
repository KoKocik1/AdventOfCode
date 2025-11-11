from helpers.array_helper import Board, Position


class AntennaAnalyzer:
    def __init__(self, board: Board):
        self.board = board

    def get_mirror_point(self, main_point: Position, secondary_point: Position) -> Position:
        new_row = main_point.row - secondary_point.row
        new_col = main_point.col - secondary_point.col
        return Position(main_point.row + new_row, main_point.col + new_col)

    def _unique_signal_characters(self) -> set[str]:
        # Build a set of unique non-empty signal characters (exclude '.')
        unique_chars = self.board.get_all_characters()
        unique_chars.remove('.')
        return unique_chars

    def find_antinodes(self, repeat: bool = False) -> set[Position]:
        """
        For each signal character, for every ordered pair of distinct antenna positions
        (A, B), add the mirror of B through A: M = A + (A - B), if it lies on the board.
        """
        antinodes: set[Position] = set()
        for character in self._unique_signal_characters():
            positions = self.board.find_all_character_positions(character)
            if len(positions) < 2:
                continue
            for main_point in positions:
                for other in positions:
                    if other == main_point:
                        continue
                    if repeat:
                        point_a = main_point
                        point_b = other
                        while True:
                            antinodes.add(point_a)
                            antinodes.add(point_b)
                            mirror_point = self.get_mirror_point(
                                point_a, point_b)
                            if self.board.is_out_of_board(mirror_point):
                                break
                            antinodes.add(mirror_point)
                            point_b = point_a
                            point_a = mirror_point
                    else:
                        mirror_point = self.get_mirror_point(main_point, other)
                        if self.board.is_out_of_board(mirror_point):
                            continue
                        antinodes.add(mirror_point)
        return antinodes

    def count_antinodes(self) -> int:
        return len(self.find_antinodes())

    def count_antinodes_lines(self) -> int:
        return len(self.find_antinodes(repeat=True))
