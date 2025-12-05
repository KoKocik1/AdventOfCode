class Range:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def is_in_range(self, number: int) -> bool:
        return self.start <= number <= self.end
    
    def is_in_ranges(self, ranges: list['Range']) -> bool:
        for range in ranges:
            if self.is_in_range(range.start) and self.is_in_range(range.end):
                return True
        return False
    
    def get_size(self) -> int:
        return self.end - self.start + 1

    def extend(self, ranges: list['Range']) -> None:
        extended = False

        for range in ranges:
            if extended:
                if self.is_in_range(range.start) and self.is_in_range(range.end):
                    ranges.remove(range)
                elif self.is_in_range(range.start):
                    extended = True
                    range.start = self.end + 1
                elif self.is_in_range(range.end):
                    extended = True
                    range.end = self.start - 1
            else:
                if range.is_in_range(self.start) and range.is_in_range(self.end):
                    extended = True
                elif range.is_in_range(self.start):
                    extended = True
                    range.end = self.end
                elif range.is_in_range(self.end):
                    extended = True
                    range.start = self.start
                elif self.is_in_range(range.start) and self.is_in_range(range.end):
                    extended = True
                    range.start = self.start
                    range.end = self.end
                
        if not extended:
            ranges.append(self)


    def ranges_to_exclude(self, check_range: 'Range') -> None:
        start_in_range = self.is_in_range(check_range.start)
        end_in_range = self.is_in_range(check_range.end)
        if start_in_range and end_in_range:
            return Range(check_range.start, check_range.end)
        elif start_in_range:
            return Range(self.start, check_range.start)
        elif end_in_range:
            return Range(self.start, check_range.start)
        else:
            return None

    def get_all_numbers(self) -> list[int]:
        return list(range(self.start, self.end + 1))
    
    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"