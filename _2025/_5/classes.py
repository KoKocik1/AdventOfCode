class Range:
    """Represents a range of integers from start to end (inclusive)."""
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def is_in_range(self, number: int) -> bool:
        """Check if a number is within this range (inclusive)."""
        return self.start <= number <= self.end

    def get_size(self) -> int:
        """Get the size of the range (number of integers it contains)."""
        return self.end - self.start + 1

    def extend(self, ranges: list['Range']) -> None:
        """Merge this range into a list of ranges, combining overlaps and adjacents."""

        to_remove = []
        new_start, new_end = self.start, self.end

        for existing in ranges:
            # Ranges overlap or are adjacent
            if not (new_end < existing.start - 1 or new_start > existing.end + 1):
                new_start = min(new_start, existing.start)
                new_end = max(new_end, existing.end)
                to_remove.append(existing)
        
        for r in to_remove:
            ranges.remove(r)

        ranges.append(Range(new_start, new_end))

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"
    

class RangeHelper:
    
    @staticmethod
    def optimize_ranges(ranges: list[Range]) -> list[Range]:
        """Optimize the ranges by merging overlapping and adjacent ranges."""
        merged_ranges: list[Range] = []
        for range_obj in ranges:
            range_obj.extend(merged_ranges)
        return merged_ranges

    @staticmethod
    def count_ingredients(ranges: list[Range], ingredients: list[int]) -> int:
        """Count the ingredients that fall within any of the given ranges."""
        count = 0
        for ingredient in ingredients:
            for range_obj in ranges:
                if range_obj.is_in_range(ingredient):
                    count += 1
                    break
        return count