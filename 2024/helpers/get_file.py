class GetFile:
    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter

    def get_row(self):
        """Generator that yields each row as a list of columns"""
        with open(self.path, 'r') as file:
            for line in file:
                yield line.strip().split(self.delimiter)


# Test example usage:
if __name__ == "__main__":
    print("Example 1: Using GetFile.get_row()")
    file_reader = GetFile(
        '/Users/krzysztofkokot/Projects/Algorithms/2024/3/data.txt', ' ')
    row_generator = file_reader.get_row()
    print(f"First row: {next(row_generator)}")
    print(f"Second row: {next(row_generator)}")
