from helpers.array_helper import Position, Board

# Constants
PROCESSED_MARKER = '+'


class Field:
    type: str
    positions: list[Position]
    iteration: int
    circuit_length: int
    walls: int

    def __init__(self, type: str, iteration: int, positions: list[Position], circuit_length: int, walls: int):
        self.type = type
        self.iteration = iteration
        self.positions = positions
        self.circuit_length = circuit_length
        self.walls = walls

    def __str__(self) -> str:
        return f"Field(type={self.type}, iteration={self.iteration}, size={len(self.positions)}, circuit={self.circuit_length})"

    def __hash__(self) -> int:
        return hash((self.type, self.iteration))


class FiledFinder:
    board: Board
    fields: list[Field]

    def __init__(self, board: Board):
        self.board = board
        self.fields = []
        self.circuit_calculator = CircuitCalculator(self.board)

    def find_fields(self):
        """Find all fields (islands) for each unique character on the board."""
        all_characters = self.board.get_all_characters()
        characters_to_process = [
            c for c in all_characters if c != PROCESSED_MARKER]
        for character in characters_to_process:
            self.search_field(character)

    def count_walls(self, point_edge_dict: dict[str, set[Position]]) -> int:
        """Count connected wall groups. Each connected component of edges with the same config is one wall."""
        walls = 0

        for config, positions in point_edge_dict.items():
            unvisited = set(positions)
            neighbors = self._get_neighbors_for_config(config)

            while unvisited:
                start = unvisited.pop()
                self._dfs_remove_connected(start, unvisited, neighbors)
                walls += 1

        return walls

    def _get_neighbors_for_config(self, config: str) -> list[tuple[int, int]]:
        """Get allowed neighbor directions based on edge configuration."""
        if config[0] == '1':  # vertical edges → check left/right
            return [(0, -1), (0, 1)]
        else:  # horizontal edges → check up/down
            return [(-1, 0), (1, 0)]

    def _dfs_remove_connected(self, start: Position, unvisited: set[Position], neighbors: list[tuple[int, int]]):
        """DFS to remove all connected positions from unvisited set."""
        stack = [start]
        while stack:
            pos = stack.pop()
            for dr, dc in neighbors:
                np = Position(pos.row + dr, pos.col + dc)
                if np in unvisited:
                    unvisited.remove(np)
                    stack.append(np)

    def search_field(self, character: str, iteration: int = 0):
        """Recursively find all islands of the same character."""
        position = self.board.find_first_character_position(character)
        if not position:
            return

        island_positions = self.find_island_positions(position, character)
        circuit_length, circuit_edges = self.circuit_calculator.calculate_circuit_for_positions(
            island_positions)

        point_edge_dict = self._group_edges_by_config(circuit_edges)
        walls = self.count_walls(point_edge_dict)

        # Mark all island positions as processed to avoid finding them again
        for pos in island_positions:
            self.board.set_character_at_position(pos, PROCESSED_MARKER)

        self.fields.append(
            Field(character, iteration, island_positions, circuit_length, walls))

        # Search for next island of the same character
        self.search_field(character, iteration + 1)

    def _group_edges_by_config(self, circuit_edges: list['Edge']) -> dict[str, set[Position]]:
        """Group edges by their configuration into a dictionary."""
        point_edge_dict: dict[str, set[Position]] = {}
        for edge in circuit_edges:
            cfg = edge.edge_config
            if cfg not in point_edge_dict:
                point_edge_dict[cfg] = set()
            point_edge_dict[cfg].add(edge.position)
        return point_edge_dict

    def find_island_positions(self, position: Position, character: str) -> list[Position]:
        """Find all connected positions (island) of the same character using BFS."""
        visited = set()
        stack = [position]
        island_positions = []
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        while stack:
            current_pos = stack.pop()

            if current_pos in visited:
                continue
            if self.board.is_out_of_board(current_pos):
                continue
            if not self.board.is_character_at_position(current_pos, character):
                continue

            visited.add(current_pos)
            island_positions.append(current_pos)

            # Check all 4 directions
            for dr, dc in neighbors:
                new_position = Position(
                    current_pos.row + dr, current_pos.col + dc)
                if new_position not in visited:
                    stack.append(new_position)

        return island_positions

    def calculate_total_score(self) -> int:
        """Calculate total score: sum of (field_size * circuit_length) for all fields."""
        return sum(len(field.positions) * field.circuit_length for field in self.fields)

    def calculate_total_score_with_walls(self) -> int:
        """Calculate total score: sum of (field_size * walls) for all fields."""
        return sum(len(field.positions) * field.walls for field in self.fields)

    def print_fields(self) -> int:
        """Legacy method name - use calculate_total_score() instead."""
        return self.calculate_total_score()

    def print_fields_with_walls(self) -> int:
        """Legacy method name - use calculate_total_score_with_walls() instead."""
        return self.calculate_total_score_with_walls()


class Edge:
    def __init__(self, position: Position, is_vertical: bool, is_before: bool, is_after: bool):
        self.position = position
        self.is_vertical = is_vertical
        self.is_before = is_before
        self.is_after = is_after

    @property
    def edge_config(self) -> str:
        return (
            f"{int(self.is_vertical)}"
            f"{int(self.is_before)}"
            f"{int(self.is_after)}"
        )


class CircuitCalculator:
    def __init__(self, board: Board):
        self.board = board
        self._num_cols = board.get_row_length()
        self._num_rows = board.get_column_length()

    def calculate_circuit_for_positions(self, positions: list[Position]) -> tuple[int, list[Edge]]:
        """Calculate perimeter (circuit length) for an island by counting vertical and horizontal edges."""
        if not positions:
            return 0, []

        vertical_count, vertical_edges = self._count_vertical_edges(positions)
        horizontal_count, horizontal_edges = self._count_horizontal_edges(
            positions)

        all_edges = vertical_edges + horizontal_edges
        return vertical_count + horizontal_count, all_edges

    def _count_vertical_edges(self, positions: list[Position]) -> tuple[int, list[Edge]]:
        """Count vertical edges (left/right boundaries) by scanning columns top to bottom."""
        if not positions:
            return 0, []

        position_set = set(positions)
        count = 0
        edges = []

        for col in range(self._num_cols):
            in_island = False
            for row in range(self._num_rows):
                cur = Position(row, col)
                is_in_island = cur in position_set

                # Entering island: left edge at current cell
                if is_in_island and not in_island:
                    count += 1
                    edges.append(Edge(cur, True, True, False))
                    in_island = True

                # Leaving island: right edge at last island cell
                elif not is_in_island and in_island:
                    last = Position(row - 1, col)
                    edges.append(Edge(last, True, False, True))
                    count += 1
                    in_island = False

            # Island extends to bottom boundary
            if in_island:
                last = Position(self._num_rows - 1, col)
                edges.append(Edge(last, True, False, True))
                count += 1

        return count, edges

    def _count_horizontal_edges(self, positions: list[Position]) -> tuple[int, list[Edge]]:
        """Count horizontal edges (top/bottom boundaries) by scanning rows left to right."""
        if not positions:
            return 0, []

        position_set = set(positions)
        count = 0
        edges = []

        for row in range(self._num_rows):
            in_island = False
            for col in range(self._num_cols):
                cur = Position(row, col)
                is_in_island = cur in position_set

                # Entering island: top edge at current cell
                if is_in_island and not in_island:
                    count += 1
                    edges.append(Edge(cur, False, True, False))
                    in_island = True

                # Leaving island: bottom edge at last island cell
                elif not is_in_island and in_island:
                    last = Position(row, col - 1)
                    edges.append(Edge(last, False, False, True))
                    count += 1
                    in_island = False

            # Island extends to right boundary
            if in_island:
                last = Position(row, self._num_cols - 1)
                edges.append(Edge(last, False, False, True))
                count += 1

        return count, edges
