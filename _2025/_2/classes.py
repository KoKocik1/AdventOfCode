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
    
    def has_repeats(self) -> list[int]:
        repeats = []
        for r in range(self.start, self.end + 1):
            range_str = str(r)
            #if len(range_str) % 2 == 0:
            half = len(range_str)//2
            for i in range(half):
                if self._check_repeat(range_str, i+1):
                    repeats.append(r)
                    break
        return repeats

    def _check_repeat(self, range_str: str, i: int) -> bool:
        # Split range_str into consecutive substrings of length i
        if i == 0 or len(range_str) % i != 0:
            return False
        parts = [range_str[j:j+i] for j in range(0, len(range_str), i)]
        first = parts[0]
        for part in parts[1:]:
            if part != first:
                return False
        return True

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"
    
    

if __name__ == "__main__":
    r = Range(1009, 1011)
    print(r.has_repeats())