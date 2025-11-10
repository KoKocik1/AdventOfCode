class Equation:
    score: int
    arguments: list[int]

    def __init__(self, score: int, arguments: list[int]):
        self.score = score
        self.arguments = arguments

    @staticmethod
    def create_from_string(score: str, arguments: str) -> 'Equation':
        equation_score = int(score)
        equation_arguments = [int(arg) for arg in arguments.split(' ')]
        return Equation(equation_score, equation_arguments)

    def __repr__(self):
        return f"Equation(score={self.score}, arguments={self.arguments})"

    def get_size(self) -> int:
        return len(self.arguments)

    def copy(self) -> 'Equation':
        return Equation(self.score, self.arguments.copy())

    def pop_argument(self) -> int:
        return self.arguments.pop(0)


class Actions:

    def add(self, a: int, b: int) -> int:
        return a + b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def solve_equation(self, equation: Equation, act_score: int = 0, idx: int = 0):
        args = equation.arguments
        if idx == len(args):
            return act_score == equation.score

        n = args[idx]
        return (
            self.solve_equation(equation, act_score + n, idx + 1) or
            self.solve_equation(equation, act_score * n, idx + 1)
        )
