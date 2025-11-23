from collections import Counter


class Robot:
    """Represents a robot with position and velocity on a 2D board."""

    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self.position = position
        self.velocity = velocity

    def move(self, steps: int) -> None:
        """Move the robot by its velocity multiplied by steps."""
        x = self.position[0] + self.velocity[0] * steps
        y = self.position[1] + self.velocity[1] * steps
        self.position = (x, y)

    def normalize_position(self, x_len: int, y_len: int) -> None:
        """Normalize position to be within board bounds using modulo."""
        x = self.position[0] % x_len
        y = self.position[1] % y_len
        # Handle negative positions
        if x < 0:
            x += x_len
        if y < 0:
            y += y_len
        self.position = (x, y)

    def __eq__(self, other: 'Robot') -> bool:
        """Check if two robots are at the same position."""
        return self.position == other.position


class Board:
    """Represents a 2D board with robots that can move."""

    def __init__(self, x_len: int, y_len: int):
        self.x_len = x_len
        self.y_len = y_len
        self.robots: list[Robot] = []

    def add_robot(self, robot: Robot) -> None:
        """Add a robot to the board."""
        self.robots.append(robot)

    def move_robots(self, steps: int) -> None:
        """Move all robots by the specified number of steps."""
        for robot in self.robots:
            robot.move(steps)
            robot.normalize_position(self.x_len, self.y_len)

    def count_robots_by_quadrant(self) -> list[int]:
        """Count robots in each of the four quadrants and return the counts."""
        mid_x = self.x_len // 2
        mid_y = self.y_len // 2

        quadrants = [
            (0, mid_x, 0, mid_y),  # Top-left
            (mid_x + 1, self.x_len, 0, mid_y),  # Top-right
            (0, mid_x, mid_y + 1, self.y_len),  # Bottom-left
            (mid_x + 1, self.x_len, mid_y + 1, self.y_len),  # Bottom-right
        ]

        return [
            self._count_robots_in_quadrant(min_x, max_x, min_y, max_y)
            for min_x, max_x, min_y, max_y in quadrants
        ]

    def _count_robots_in_quadrant(self, min_x: int, max_x: int, min_y: int, max_y: int) -> int:
        """Count robots within the specified quadrant boundaries."""
        return sum(
            1 for robot in self.robots
            if min_x <= robot.position[0] < max_x and min_y <= robot.position[1] < max_y
        )

    def _count_robots_at_position(self, x: int, y: int) -> int:
        """Count how many robots are at the specified position."""
        return sum(1 for robot in self.robots if robot.position == (x, y))

    def has_no_overlaps(self) -> bool:
        """Check if all robots are at unique positions (no overlaps)."""
        position_counts = Counter(robot.position for robot in self.robots)
        return all(count == 1 for count in position_counts.values())

    def print_board(self) -> None:
        """Print a visual representation of the board."""
        for x in range(self.x_len):
            for y in range(self.y_len):
                count = self._count_robots_at_position(x, y)
                print(count if count > 0 else '.', end='')
            print()
