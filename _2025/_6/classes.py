class ColumnScore:
    """Calculates score for a column based on numbers and math operation."""
    
    def __init__(self, column: list[int], math_character: str):
        self.column = column
        self.math_character = math_character

    def calculate_score(self) -> int:
        """Calculate the score by applying the math operation to all numbers in the column."""
        if not self.column:
            return 0
        
        if self.math_character == '+':
            return sum(self.column)
        elif self.math_character == '*':
            result = 1
            for number in self.column:
                result *= number
            return result
        else:
            raise ValueError(f"Unsupported math character: {self.math_character}")
    
