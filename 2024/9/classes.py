from helpers import GetFile


class DiscSpace:
    def __init__(self):
        self.disc_space = []

    def load_disc_space(self, file: GetFile):
        is_file = True
        file_ID = 0
        for row in file.get_row():
            for char in row:
                char_to_int = int(char)
                for _ in range(char_to_int):
                    if is_file:
                        self.disc_space.append(file_ID)
                    else:
                        self.disc_space.append(-1)
                if is_file:
                    file_ID += 1
                is_file = not is_file
        self.file_size = self._calculate_file_size()

    def _calculate_file_size(self) -> int:
        count = 0
        for i in range(len(self.disc_space)):
            if self.disc_space[i] != -1:
                count += 1
        return count

    def _print_disc_space(self):
        for i in range(len(self.disc_space)):
            if self.disc_space[i] == -1:
                print(".")
            else:
                print(self.disc_space[i])

    def __str__(self):
        return f"DiscSpace(disc_space={self._print_disc_space()})"

    def _find_first_empty_space_position(self, act_position: int) -> int:
        for i in range(act_position, len(self.disc_space)):
            if self.disc_space[i] == -1:
                return i
        return None

    def _find_last_number_position(self, act_position: int) -> int:
        for i in range(act_position, -1, -1):
            if self.disc_space[i] != -1:
                return i
        return None

    def remove_empty_slots(self):
        self.disc_space = [slot for slot in self.disc_space if slot != -1]

    def clear_disc_space(self):
        empty_position = self._find_first_empty_space_position(0)
        number_position = self._find_last_number_position(
            len(self.disc_space) - 1)

        while empty_position is not None and number_position is not None and empty_position < number_position:
            # move the block from number_position to the first empty slot
            self.disc_space[empty_position], self.disc_space[number_position] = (
                self.disc_space[number_position],
                -1,
            )
            empty_position = self._find_first_empty_space_position(
                empty_position + 1)
            number_position = self._find_last_number_position(
                number_position - 1)

    def calculate_checksum(self) -> int:
        checksum = 0
        for i in range(len(self.disc_space)):
            checksum += self.disc_space[i] * i
        return checksum
