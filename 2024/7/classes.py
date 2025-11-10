class Equation:
    score: int
    arguments: list[int]

    def __init__(self, score: int, arguments: list[int]):
        self.score = score
        self.arguments = arguments

    @staticmethod
    def create_from_string(score: str, arguments: str):
        equation_score = int(score)
        equation_arguments = [int(arg) for arg in arguments.split(' ')]
        return Equation(equation_score, equation_arguments)

    def __repr__(self):
        return f"Equation(score={self.score}, arguments={self.arguments})"

    def get_size(self):
        return len(self.arguments)

    def copy(self):
        # Creates a deep copy of the Equation instance
        return Equation(self.score, self.arguments.copy())

    def pop_argument(self):
        return self.arguments.pop(0)


class Actions:

    def add(self, a: int, b: int):
        return a + b

    def multiply(self, a: int, b: int):
        return a * b

    def solve_equation(self, equation: Equation, act_score: int = 0, history: str = ''):
        if equation.get_size() == 0:
            return act_score == equation.score
        figure = equation.pop_argument()
        scoreAdd = self.add(act_score, figure)
        scoreAddHistory = f'{history} + {figure}'
        scoreMultiply = self.multiply(act_score, figure)
        scoreMultiplyHistory = f'{history} * {figure}'
        return self.solve_equation(equation.copy(), scoreAdd, scoreAddHistory) or self.solve_equation(equation.copy(), scoreMultiply, scoreMultiplyHistory)
