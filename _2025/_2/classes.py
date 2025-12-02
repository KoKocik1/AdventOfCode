class Range:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def has_overlaps(self) -> list[int]:
        overlaps = []
        for r in range(self.start, self.end + 1):
            range_str = str(r)
            if len(range_str) % 2 == 0:
                first_half = range_str[:len(range_str)//2]
                second_half = range_str[len(range_str)//2:]
                if first_half == second_half:
                    overlaps.append(r)
        return overlaps

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"