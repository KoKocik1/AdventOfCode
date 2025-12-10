from pathlib import Path

from helpers import GetFile, time_and_print
from classes import Indicators, Indicator

def part1(data: Indicators) -> int:
    return data.find_states()

def part2(data: Indicators) -> int:
    return data.find_joltage()

def get_data(file: GetFile) -> Indicators:
    all_indicators = Indicators()

    for line in file.get_row():
        result = list(line[0].strip('[]'))
        buttons = []
        joltage = []
        for l in line[1:]:
            if l.startswith('('):
                buttons.append(l.strip('()').split(','))
            elif l.startswith('{'):
                joltage.extend(l.strip('{}').split(','))
        buttons = [list(map(int, b)) for b in buttons]
        joltage = [int(j) for j in joltage]
        indicator = Indicator(result, buttons, joltage)
        all_indicators.indicators.append(indicator)
    return all_indicators

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=' ')
    data = get_data(file)
    
    result1 = time_and_print("Part 1", part1, data)
    result2 = time_and_print("Part 2", part2, data)


if __name__ == "__main__":
    main()
