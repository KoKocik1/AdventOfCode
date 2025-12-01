class GetFile:
    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter

    def get_row(self):
        """Generator that yields each row as a list of columns"""
        with open(self.path, 'r') as file:
            for line in file:
                stripped = line.strip()
                # If delimiter is empty string or None, split into characters
                if not self.delimiter:
                    yield list(stripped)
                else:
                    yield stripped.split(self.delimiter)

    def get_2d_array(self) -> list[list[str]]:
        """Return the file as a 2D array (list of lists)."""
        return [row for row in self.get_row()]
    
    def get_string_list(self) -> list[str]:
        return [row[0] for row in self.get_row()]


# Test example usage:
if __name__ == "__main__":
    print("Example 1: Using GetFile.get_row()")
    file_reader = GetFile(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/3/data.txt', ' ')
    row_generator = file_reader.get_row()
    # print(f"First row: {next(row_generator)}")
    # print(f"Second row: {next(row_generator)}")
    file_reader = GetFile(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/4/test.txt', '')

    two_d_array = file_reader.get_2d_array()

    for row in range(len(two_d_array)):
        for col in range(len(two_d_array[0])):
            print(two_d_array[row][col], end=' ')
        print()
