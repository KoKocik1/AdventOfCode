from typing import Optional, Tuple

# Constants for button costs and limits
BUTTON_A_COST = 3
BUTTON_B_COST = 1
MAX_BUTTON_PRESSES = 101


class Button:
    def __init__(self, name: str, x: int, y: int):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Button(name={self.name}, x={self.x}, y={self.y})"


class Prize:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Prize(x={self.x}, y={self.y})"


class ButtonFactory:
    @staticmethod
    def create_from_string(name: str, x: str, y: str) -> Button:
        name = name.split(':')[0].strip()
        x = int(x.split('X+')[1].split(',')[0])
        y = int(y.split('Y+')[1].split(',')[0])
        return Button(name, x, y)


class PrizeFactory:
    @staticmethod
    def create_from_string(x: str, y: str) -> Prize:
        x = int(x.split('X=')[1].split(',')[0])
        y = int(y.split('Y=')[1].split(',')[0])
        return Prize(x, y)


class Machine:
    def __init__(self, button_a: Button, button_b: Button, prize: Prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __str__(self) -> str:
        return f"Machine(button_a={self.button_a}, button_b={self.button_b}, prize={self.prize})"


class DeterminantCalculator:
    @staticmethod
    def compute(ax: int, ay: int, bx: int, by: int) -> int:
        return ax * by - ay * bx


class CramerCalculator:
    @staticmethod
    def solve(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> Optional[Tuple[int, int]]:
        D = DeterminantCalculator.compute(ax, ay, bx, by)

        if D == 0:
            return None

        Dx = DeterminantCalculator.compute(px, py, bx, by)
        Dy = DeterminantCalculator.compute(ax, ay, px, py)
        a = Dx // D
        b = Dy // D

        return (a, b) if Dx % D == 0 and Dy % D == 0 else None


class BruteforceSolver:
    @staticmethod
    def solve(ax: int, ay: int, bx: int, by: int, px: int, py: int) -> Optional[Tuple[int, int]]:
        best = None
        best_cost = float('inf')

        for a in range(MAX_BUTTON_PRESSES + 1):
            for b in range(MAX_BUTTON_PRESSES + 1):
                if a * ax + b * bx != px:
                    continue
                if a * ay + b * by != py:
                    continue

                cost = BUTTON_A_COST * a + BUTTON_B_COST * b
                if cost < best_cost:
                    best_cost = cost
                    best = (a, b)

        return best


class MachineCalculator:
    def __init__(self, machine: 'Machine'):
        self.machine = machine

    def _get_coordinates(self) -> Tuple[int, int, int, int, int, int]:
        """Extract all coordinates from the machine."""
        return (
            self.machine.button_a.x,
            self.machine.button_a.y,
            self.machine.button_b.x,
            self.machine.button_b.y,
            self.machine.prize.x,
            self.machine.prize.y
        )

    def _calculate_cost(self, a: int, b: int) -> int:
        """Calculate the cost given button press counts."""
        return BUTTON_A_COST * a + BUTTON_B_COST * b

    def calculate_machine(self) -> int:
        """Calculate the minimal cost to win the prize using Cramer's rule or brute force."""
        ax, ay, bx, by, px, py = self._get_coordinates()

        # Try Cramer's method first
        result = CramerCalculator.solve(ax, ay, bx, by, px, py)
        if result:
            a, b = result
            return self._calculate_cost(a, b)

        # If Cramer didn't give a result, try brute-force
        result = BruteforceSolver.solve(ax, ay, bx, by, px, py)
        if result:
            a, b = result
            return self._calculate_cost(a, b)

        # No solution found
        return 0

    def calculate_with_limit(self) -> int:
        """Calculate cost with a limit on button presses using iterative approach."""
        ax, ay, bx, by, px, py = self._get_coordinates()

        a = 0
        while True:
            missing_x = px - a * ax
            missing_y = py - a * ay

            if missing_x < 0 or missing_y < 0:
                return 0

            if missing_x % bx == 0 and missing_y % by == 0:
                b_x = missing_x // bx
                b_y = missing_y // by

                if b_x == b_y and 0 <= b_x <= MAX_BUTTON_PRESSES:
                    return self._calculate_cost(a, b_x)

            a += 1
            if a > MAX_BUTTON_PRESSES:
                return 0
