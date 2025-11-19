import math
from sympy import Matrix


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


class Mashine:
    def __init__(self, button_a: Button, button_b: Button, prize: Prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __str__(self) -> str:
        return f"Mashine(button_a={self.button_a}, button_b={self.button_b}, prize={self.prize})"


class DeterminantCalculator:
    @staticmethod
    def compute(ax, ay, bx, by) -> int:
        return ax * by - ay * bx


class CramerCalculator:
    @staticmethod
    def solve(ax, ay, bx, by, px, py):

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
    def solve(ax, ay, bx, by, r1, r2):
        best = None
        best_cost = float('inf')

        for a in range(0, 101):
            for b in range(0, 101):
                if a * ax + b * bx != r1:
                    continue
                if a * ay + b * by != r2:
                    continue

                cost = 3 * a + b
                if cost < best_cost:
                    best_cost = cost
                    best = (a, b)

        return best


class MashineCalculator:
    mashine: Mashine

    def __init__(self, mashine):
        self.mashine = mashine

    def calculate_mashine(self, limit: int = None) -> int:
        ax = self.mashine.button_a.x
        ay = self.mashine.button_a.y
        bx = self.mashine.button_b.x
        by = self.mashine.button_b.y
        px = self.mashine.prize.x
        py = self.mashine.prize.y

        # # 1. Try Cramer method
        result = CramerCalculator.solve(ax, ay, bx, by, px, py)
        if result:
            a, b = result
            if limit is None or (0 <= a <= limit + 1 and 0 <= b <= limit + 1):
                # print(f"CramerSolver: {a}, {b}")
                return a * 3 + b * 1

        # 2. If Cramer didn't give a result → brute-force
        result = BruteforceSolver.solve(ax, ay, bx, by, px, py)
        if result:
            a, b = result
            # print(f"BruteforceSolver: {a}, {b}")
            return a * 3 + b * 1

        # 3. No solution
        return 0

    def calculate_with_limit(self) -> int:
        ax = self.mashine.button_a.x
        ay = self.mashine.button_a.y
        bx = self.mashine.button_b.x
        by = self.mashine.button_b.y
        px = self.mashine.prize.x
        py = self.mashine.prize.y

        a = -1
        while True:
            a += 1
            missing_x = px - a*ax
            missing_y = py - a*ay
            if missing_x < 0 or missing_y < 0:
                return 0
            if missing_x % bx != 0 or missing_y % by != 0:
                continue
            b_x = missing_x // bx
            b_y = missing_y // by

            if b_x != b_y:
                continue
            if 0 <= b_x <= 101:
                return 3*a + 1*b_x
