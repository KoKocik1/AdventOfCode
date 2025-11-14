
class Stones:
    def __init__(self, stones: list[str]):
        self.stones = [int(stone) for stone in stones]

    def _has_even_nnumber(self, stone: int) -> bool:
        s = str(stone)
        return len(s) % 2 == 0

    def _split_stone(self, stone: int) -> list[int]:
        s = str(stone)
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]

    def _multiply_stones(self, stone: int) -> list[int]:
        if stone == 0:
            return [1]
        if self._has_even_nnumber(stone):
            return self._split_stone(stone)
        else:
            return [stone*2024]

    def blink(self) -> None:
        new_stones = []
        for stone in self.stones:
            new_stones.extend(self._multiply_stones(stone))
        self.stones = new_stones
        # print(f"Number of stones: {self.number_of_stones()}")

    def number_of_stones(self) -> int:
        return len(self.stones)

    def __str__(self) -> str:
        return ' '.join(str(stone) for stone in self.stones)


class RecursiveStones:
    def __init__(self, stones: list[str]):
        self.stones = [int(stone) for stone in stones]
        self._cache = {}  # Memoization cache: (stone, blinks) -> count

    def _has_even_nnumber(self, stone: int) -> bool:
        s = str(stone)
        return len(s) % 2 == 0

    def _split_stone(self, stone: int) -> list[int]:
        s = str(stone)
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]

    def _multiply_stones(self, stone: int) -> list[int]:
        if stone == 0:
            return [1]
        if self._has_even_nnumber(stone):
            return self._split_stone(stone)
        else:
            return [stone*2024]

    def recursive_blink(self, blinks: int) -> int:
        self._cache.clear()  # Clear cache for new calculation
        count = 0
        for stone in self.stones:
            count += self._blink(stone, blinks)
        return count

    def _blink(self, stone: int, blinks: int) -> int:
        # Check cache first
        cache_key = (stone, blinks)
        if cache_key in self._cache:
            return self._cache[cache_key]

        # Base case: no more blinks
        if blinks == 0:
            return 1

        # Recursive case: process new stones
        new_stones = self._multiply_stones(stone)
        count = 0
        for new_stone in new_stones:
            count += self._blink(new_stone, blinks - 1)

        # Cache and return result
        self._cache[cache_key] = count
        return count
