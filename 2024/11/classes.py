class Stones:
    def __init__(self, stones: list[int]):
        self.stones = stones

    @staticmethod
    def create_from_string(stones: list[str]) -> 'Stones':
        return Stones([int(stone) for stone in stones])

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

    def number_of_stones(self) -> int:
        return len(self.stones)

    def __str__(self) -> str:
        return ' '.join(str(stone) for stone in self.stones)
