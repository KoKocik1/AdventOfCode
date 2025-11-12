from helpers import GetFile


class File:
    def __init__(self):
        self.file_ID = -1
        self.file_size = 0
        self.position = 0

    def set_file_ID(self, file_ID: int):
        self.file_ID = file_ID

    def set_position(self, position: int):
        self.position = position
        self.file_size += 1


class EmptySpace:
    def __init__(self):
        self.size = 0
        self.first_position = 0

    def add_empty_space(self, first_position: int):
        if self.size == 0:
            self.first_position = first_position
            self.size = 1
        else:
            self.size += 1


class DiscSpace:
    def __init__(self):
        self.disc_space = []

    def load_disc_space(self, file: GetFile):
        is_file = True
        file_ID = 0
        empty_ID = -1
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

    def _find_first_empty_space_for_file(self, file: File) -> EmptySpace:
        empty_space = EmptySpace()
        for i in range(0, file.position):
            if self.disc_space[i] == -1:
                empty_space.add_empty_space(i)
                if empty_space.size == file.file_size:
                    return empty_space
            else:
                empty_space.size = 0
        return None

    def _find_last_file_position(self, act_position: int, last_file_IDs: set[int]) -> File:
        found_file = False
        file = File()
        for i in range(act_position, -1, -1):
            if self.disc_space[i] not in last_file_IDs and self.disc_space[i] != -1 and (not found_file or self.disc_space[i] == file.file_ID):
                file.set_file_ID(self.disc_space[i])
                file.set_position(i)
                found_file = True
            elif found_file:
                return file
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

    def clear_disc_space_all_files(self):
        last_file_IDs = set()
        file_to_move = self._find_last_file_position(
            len(self.disc_space) - 1, last_file_IDs)

        empty_position = self._find_first_empty_space_for_file(file_to_move)

        while file_to_move is not None or file_to_move.position <= file_to_move.file_size:
            if empty_position is not None:
                difference = empty_position.first_position - file_to_move.position
                # move the block from number_position to the first empty slot
                for i in range(file_to_move.position, file_to_move.position + file_to_move.file_size):
                    self.disc_space[i + difference] = self.disc_space[i]
                    last_file_IDs.add(self.disc_space[i])
                    self.disc_space[i] = -1
            file_to_move = self._find_last_file_position(
                file_to_move.position - 1, last_file_IDs)
            if file_to_move is None or file_to_move.file_ID == 0:
                break
            empty_position = self._find_first_empty_space_for_file(
                file_to_move)

    def calculate_checksum(self) -> int:
        checksum = 0
        for i in range(len(self.disc_space)):
            if self.disc_space[i] != -1:
                checksum += self.disc_space[i] * i
        return checksum
