import re
from pathlib import Path

from helpers import GetFile


mul_regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
do_regex = re.compile(r"do\(\)")
dont_regex = re.compile(r"don't\(\)")


def calculate_mul_sum(text):
    """Calculate the sum of all mul(a,b) operations in the text."""
    matches = mul_regex.findall(text)
    total = 0
    for match in matches:
        num1, num2 = map(int, match)
        total += num1 * num2
    return total


def remove_dont_sections(text):
    """Remove sections from don't() to do() (or to the end if no do() found)."""
    while True:
        dont = dont_regex.search(text)
        if not dont:
            break

        dont_start = dont.start()
        dont_end = dont.end()
        text_after_dont = text[dont_end:]
        do = do_regex.search(text_after_dont)

        if do:
            # Remove from don't() to the end of do()
            do_end_in_full_text = dont_end + do.end()
            text = text[:dont_start] + text[do_end_in_full_text:]
        else:
            # Remove from don't() to the end of text
            text = text[:dont_start]

    return text


def part1(file):
    """Part 1: Sum of all mul(a,b) operations in all rows."""
    total = 0
    for row in file.get_row():
        text = ''.join(row)
        total += calculate_mul_sum(text)
    return total


def part2(file):
    """Part 2: Sum of mul(a,b) after removing don't()...do() sections."""
    # Join all rows into a single text
    text = ''.join(''.join(row) for row in file.get_row())

    # Remove don't()...do() sections
    processed_text = remove_dont_sections(text)

    # Calculate sum of mul() in the processed text
    return calculate_mul_sum(processed_text)


def main():
    """Main function that runs both parts of the task."""
    data_file = Path(__file__).parent / 'data.txt'
    delimiter = ' '

    # Part 1: Sum of all mul() in all rows
    file1 = GetFile(str(data_file), delimiter)
    result1 = part1(file1)
    print(f"Part 1: {result1}")

    # Part 2: Sum of mul() after removing don't()...do() sections
    file2 = GetFile(str(data_file), delimiter)
    result2 = part2(file2)
    print(f"Part 2: {result2}")


if __name__ == "__main__":
    main()
