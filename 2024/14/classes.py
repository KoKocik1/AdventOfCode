class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]):
        self.position = position
        self.velocity = velocity

    def move(self, steps: int):
        self.position = (self.position[0] + self.velocity[0]
                         * steps, self.position[1] + self.velocity[1] * steps)

    def normalize_position(self, x_len: int, y_len: int):
        self.position = (self.position[0] % x_len, self.position[1] % y_len)

    def __eq__(self, other: 'Robot') -> bool:
        return self.position[0] == other.position[0] and self.position[1] == other.position[1]


class Board:
    x_len: int
    y_len: int
    robots: list[Robot]

    def __init__(self, x_len: int, y_len: int):
        self.x_len = x_len
        self.y_len = y_len
        self.robots = []

    def add_robot(self, robot: Robot):
        self.robots.append(robot)

    def move_robots(self, steps: int):
        for robot in self.robots:
            robot.move(steps)
            robot.normalize_position(self.x_len, self.y_len)

    def count_robots(self) -> list[list[Robot]]:
        mid_x = self.x_len // 2
        mid_y = self.y_len // 2
        quadrants = [
            (0, mid_x, 0, mid_y),
            (mid_x+1, self.x_len, 0, mid_y),
            (0, mid_x, mid_y+1, self.y_len),
            (mid_x+1, self.x_len, mid_y+1, self.y_len)
        ]
        return [
            self._count_robots_at_quadrant(min_x, max_x, min_y, max_y)
            for min_x, max_x, min_y, max_y in quadrants
        ]

    def _count_robots_at_quadrant(self, min_x: int, max_x: int, min_y: int, max_y: int) -> int:
        count = 0
        for robot in self.robots:
            if robot.position[0] >= min_x and robot.position[0] < max_x and robot.position[1] >= min_y and robot.position[1] < max_y:
                count += 1
        return count

    def _count_robots_at_position(self, x: int, y: int) -> int:
        count = 0
        for robot in self.robots:
            if robot.position[0] == x and robot.position[1] == y:
                count += 1
        return count

    def no_repeats(self):
        for robot in self.robots:
            if self._count_robots_at_position(robot.position[0], robot.position[1]) > 1:
                return False
        return True

    def print_board(self):
        for x in range(self.x_len):
            for y in range(self.y_len):
                occours = self._count_robots_at_position(x, y)
                if occours > 0:
                    print(occours, end='')
                else:
                    print('.', end='')
            print()
