from helpers.array_helper import Position, Board
from helpers.array_helper import Player


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
        all_characters = self.board.get_all_characters()
        # Filter out '+' which we use as a marker for processed positions
        characters_to_process = [c for c in all_characters if c != '+']
        for character in characters_to_process:
            self.search_field(character)

    def count_walls(self, point_edge_dict) -> int:
        walls = 0

        for config, positions in point_edge_dict.items():
            unvisited = set(positions)

            # wybór dozwolonych sąsiadów na podstawie edge_config
            if config[0] == '1':
                # vertical → sprawdzamy tylko lewo/prawo
                neighbors = [(0, -1), (0, 1)]
            else:
                # horizontal → sprawdzamy tylko góra/dół
                neighbors = [(-1, 0), (1, 0)]

            # każda spójna grupa = 1 wall
            while unvisited:
                start = unvisited.pop()
                stack = [start]

                while stack:
                    pos = stack.pop()

                    for dr, dc in neighbors:
                        np = Position(pos.row + dr, pos.col + dc)

                        if np in unvisited:
                            unvisited.remove(np)
                            stack.append(np)

                # ukończony DFS → 1 wall
                walls += 1

        return walls

    def search_field(self, character: str, iteration: int = 0):
        position = self.board.find_first_character_position(character)
        if position:
            # Find all connected positions (island) - collect positions first
            island_positions = self.find_island_positions(position, character)
            # Calculate circuit length for this specific island
            circuit_length, circuit_edges = self.circuit_calculator.calculate_circuit_for_positions(
                island_positions)
            # INSERT_YOUR_CODE
            # circuit_edges is expected to be a list of tuples: (position, edge_config)
            point_edge_dict = {}

            for edge in circuit_edges:
                cfg = edge.edge_config
                if cfg not in point_edge_dict:
                    point_edge_dict[cfg] = set()
                point_edge_dict[cfg].add(edge.position)

            walls = self.count_walls(point_edge_dict)

            # Mark all island positions as '+' to avoid finding them again
            for pos in island_positions:
                self.board.set_character_at_position(pos, '+')
            # Create field with found positions
            self.fields.append(
                Field(character, iteration, island_positions, circuit_length, walls))
            # Search for next island of the same character
            self.search_field(character, iteration + 1)

    def find_island_positions(self, position: Position, character: str) -> list[Position]:
        """Find all connected positions (island) of the same character and return them as a list"""
        visited = set()
        stack = [position]
        island_positions = []

        while stack:
            current_pos = stack.pop()

            # Skip if already visited or out of bounds
            if current_pos in visited:
                continue
            if self.board.is_out_of_board(current_pos):
                continue
            if not self.board.is_character_at_position(current_pos, character):
                continue

            # Mark as visited and add to island
            visited.add(current_pos)
            island_positions.append(current_pos)

            # Check all 4 directions
            player = Player(self.board)
            for _ in range(4):
                new_position = player.move(current_pos)
                player.turn_right()
                if new_position and new_position not in visited:
                    if self.board.is_character_at_position(new_position, character):
                        stack.append(new_position)

        return island_positions

    def print_fields(self):
        count = 0
        for field in self.fields:
            # print(field.type)
            # print(field.iteration)
            score = len(field.positions) * field.circuit_length
            # print(f"{len(field.positions)} * {field.circuit_length} = {score}")
            count += score
        return count

    def print_fields_with_walls(self):
        count = 0
        for field in self.fields:
            # print(field.type)
            score = len(field.positions) * field.walls
            # print(
            #     f"fields: {len(field.positions)}* walls: {field.walls} = {score}")
            count += score
        return count


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

    def calculate_circuit_for_positions(self, positions: list[Position]) -> tuple[int, list]:
        """Calculate perimeter (circuit length) for an island by counting vertical and horizontal edges"""
        edges = []
        if not positions:
            return 0, edges

        vertical_edges, vertical_edges_list = self._count_vertical_edges(
            positions)
        horizontal_edges, horizontal_edges_list = self._count_horizontal_edges(
            positions)
        edges.extend(vertical_edges_list)
        edges.extend(horizontal_edges_list)
        return vertical_edges + horizontal_edges, edges

    def _count_vertical_edges(self, positions: list[Position]) -> tuple[int, list]:
        """Count vertical edges (left/right boundaries) by scanning columns."""
        if not positions:
            return 0, []

        position_set = set(positions)
        count = 0
        edges = []

        num_cols = self.board.get_row_length()      # liczba kolumn
        num_rows = self.board.get_column_length()   # liczba wierszy

        for col in range(num_cols):
            in_island = False
            # przechodzimy w dół po wierszach
            for row in range(num_rows):
                cur = Position(row, col)
                is_in_island = cur in position_set

                # wejście do wyspy (non-island -> island): left edge at current cell
                if is_in_island and not in_island:
                    count += 1
                    edges.append(Edge(cur, True, True, False))
                    in_island = True

                # wyjście z wyspy (island -> non-island): right edge at last island cell (row-1)
                elif not is_in_island and in_island:
                    last = Position(row - 1, col)
                    edges.append(Edge(last, True, False, True))
                    count += 1
                    in_island = False

            # jeśli wyspa dochodziła do dolnej granicy (byliśmy w wyspie przy ostatnim wierszu)
            if in_island:
                last = Position(num_rows - 1, col)
                edges.append(Edge(last, True, False, True))
                count += 1

        return count, edges

    def _count_horizontal_edges(self, positions: list[Position]) -> tuple[int, list]:
        """Count horizontal edges (top/bottom boundaries) by scanning rows."""
        if not positions:
            return 0, []

        position_set = set(positions)
        count = 0
        edges = []

        num_cols = self.board.get_row_length()      # liczba kolumn
        num_rows = self.board.get_column_length()   # liczba wierszy

        for row in range(num_rows):
            in_island = False
            # przechodzimy po kolumnach w prawo
            for col in range(num_cols):
                cur = Position(row, col)
                is_in_island = cur in position_set

                # wejście do wyspy (non-island -> island): top edge at current cell
                if is_in_island and not in_island:
                    count += 1
                    edges.append(Edge(cur, False, True, False))
                    in_island = True

                # wyjście z wyspy (island -> non-island): bottom edge at last island cell (col-1)
                elif not is_in_island and in_island:
                    last = Position(row, col - 1)
                    edges.append(Edge(last, False, False, True))
                    count += 1
                    in_island = False

            # jeśli wyspa dochodziła do prawej granicy
            if in_island:
                last = Position(row, num_cols - 1)
                edges.append(Edge(last, False, False, True))
                count += 1

        return count, edges
