class Range:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    def has_overlaps(self) -> list[int]:
        """Find numbers where first half equals second half (e.g., 1212, 3434)."""
        overlaps = []
        for num in range(self.start, self.end + 1):
            num_str = str(num)
            if len(num_str) % 2 == 0:
                half_len = len(num_str) // 2
                if num_str[:half_len] == num_str[half_len:]:
                    overlaps.append(num)
        return overlaps
    
    def has_repeats(self) -> list[int]:
        """Find numbers with repeating patterns (e.g., 1212, 123123)."""
        repeats = []
        for num in range(self.start, self.end + 1):
            num_str = str(num)
            half_len = len(num_str) // 2
            for pattern_len in range(1, half_len + 1):
                if self._check_repeat(num_str, pattern_len):
                    repeats.append(num)
                    break
        return repeats

    def _check_repeat(self, num_str: str, pattern_len: int) -> bool:
        """Check if number string repeats a pattern of given length."""
        if pattern_len == 0 or len(num_str) % pattern_len != 0:
            return False
        parts = [num_str[j:j+pattern_len] for j in range(0, len(num_str), pattern_len)]
        return all(part == parts[0] for part in parts[1:])

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"
    
    

if __name__ == "__main__":
    r = Range(1009, 1011)
    print(r.has_repeats())