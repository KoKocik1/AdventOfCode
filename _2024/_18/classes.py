from helpers.array_helper import Position, Board, Player
from collections import deque

class PathFinder:
    """Finds the shortest path from start to end position on a board."""
    
    def __init__(self, board: Board):
        self.board = board
        self.player = Player(board)
        self.position_costs = {}
        self.positions_to_visit = deque()
        self.queue_costs = {}
        self.start_position = Position(0, 0)
        self.end_position = Position(
            board.get_column_length() - 1, 
            board.get_row_length() - 1
        )
        
    def clear_board(self) -> None:
        self.position_costs.clear()
        self.positions_to_visit.clear()
        self.queue_costs.clear()
    
    def add_new_obstacle(self, position: Position) -> None:
        """Add a new obstacle to the board."""
        self.board.set_character_at_position(position, '#')
        
    def find_shortest_path(self) -> int:
        """Find the shortest path from start to end position."""
        self.clear_board()
        self.position_costs[self.start_position] = 0
        self.positions_to_visit.append((self.start_position, 0))
        
        while self.positions_to_visit:
            act_position, cost = self.positions_to_visit.popleft()
            
            # Remove from queue_costs when processing
            if act_position in self.queue_costs:
                del self.queue_costs[act_position]
            
            # Skip if we've already found a better path to this position
            if act_position in self.position_costs and self.position_costs[act_position] < cost:
                continue
            
            self.position_costs[act_position] = cost
            
            if act_position == self.end_position:
                return cost
            
            self._explore_neighbors(act_position, cost)
        
        if self.end_position not in self.position_costs:
            return None
        return self.position_costs[self.end_position]
    
    def _explore_neighbors(self, position: Position, cost: int) -> None:
        """Explore all valid neighboring positions."""
        
        # print("Checking neighbors of", position, "with cost", cost)
        # print("-")
        for direction in self.player.directions:
            self.player.set_direction(direction)
            new_position = self.player.move(position)
            #print(direction, new_position)
            self.add_to_positions_to_visit(new_position, cost + 1)
                #print(cost+1)
        #self.draw_path()

    def draw_path(self) -> None:
        """Draw the path on the board."""
        # last_cost = self.position_costs[self.end_position]
        # for position, cost in self.position_costs.items():
        #     new_board[position.row][position.col] = str(cost)
        
        for row in range(self.board.get_column_length()):
            for col in range(self.board.get_row_length()):
                position = Position(row, col)
                cost = self.position_costs.get(position)
                if cost is not None:
                    self.board.set_character_at_position(position, str(cost))
                print(self.board.get_character(position), end='\t')
            print('\n')
        
        print("--------------------------------")

    def add_to_positions_to_visit(self, position: Position, cost: int) -> None:
        """Add a position to the positions to visit."""
        if not position or not self.board.is_character_at_position(position, '.'):
            return
        
        new_cost = cost
    
        # Skip if already visited with better cost
        if position in self.position_costs and self.position_costs[position] < new_cost:
            return

        # Check if position is already in queue with better or equal cost
        if position in self.queue_costs and self.queue_costs[position] <= new_cost:
            return

        # Add to queue (or update if already there with worse cost)
        self.queue_costs[position] = new_cost
        self.positions_to_visit.append((position, new_cost))
