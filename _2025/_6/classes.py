class ColumnScore:
    def __init__(self, column: list[int], math_character: str):
        self.column = column
        self.math_character = math_character
        self.score = 0

    def calculate_score(self) -> int:
        for number in self.column:
            self.add_to_score(number)
        return self.score

    def add_to_score(self, number: int):
        if self.math_character == '+':
            self.score += number
        elif self.math_character == '*':
            if self.score == 0:
                self.score = 1
            self.score *= number

    def get_score(self) -> int:
        return self.score
    
