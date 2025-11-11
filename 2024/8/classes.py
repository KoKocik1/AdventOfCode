from helpers.array_helper import Board, Position


class AntennaAnalyzer:
    def __init__(self, board: Board):
        self.board = board
        self.antinodes: set[Position] = set()

    def get_mirror_point(self, main_point: Position, secondary_point: Position) -> Position:
        new_row = main_point.row - secondary_point.row
        new_col = main_point.col - secondary_point.col
        return Position(main_point.row + new_row, main_point.col + new_col)

    def _unique_signal_characters(self) -> set[str]:
        # Build a set of unique non-empty signal characters (exclude '.')
        return {ch for ch in self.board.get_all_characters() if ch != '.'}

    def find_antinodes(self, func) -> set[Position]:
        """
        For each signal character, for every ordered pair of distinct antenna positions
        (A, B), add the mirror of B through A: M = A + (A - B), if it lies on the board.
        """
        self.antinodes: set[Position] = set()
        for character in self._unique_signal_characters():
            positions = self.board.find_all_character_positions(character)
            if len(positions) < 2:
                continue
            for main_point in positions:
                for other in positions:
                    if other == main_point:
                        continue
                    func(main_point, other)

    def count_sinlge_antinodes(self) -> int:
        self.find_antinodes(self._add_single_antinodes)
        return len(self.antinodes)

    def count_recursive_antinodes(self) -> int:
        self.find_antinodes(self._add_antinodes_recursive)
        return len(self.antinodes)

    def _add_single_antinodes(self, main_point, other):
        mirror_point = self.get_mirror_point(main_point, other)
        if not self.board.is_out_of_board(mirror_point):
            self.antinodes.add(mirror_point)

    def _add_antinodes_recursive(self, point_a, point_b):
        # Add current points
        self.antinodes.add(point_a)
        self.antinodes.add(point_b)

        mirror_point = self.get_mirror_point(point_a, point_b)
        if self.board.is_out_of_board(mirror_point):
            return  # recursion stop condition

        self.antinodes.add(mirror_point)
        # Recurse with new pair
        self._add_antinodes_recursive(mirror_point, point_a)
