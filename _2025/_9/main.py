from pathlib import Path
import matplotlib.pyplot as plt
from helpers import GetFile, time_and_print, Position, Board, BoardArray
from _2025._9.classes import RectanglArea, RedGreenField

def part1(points: list[Position]) -> int:
    rectangle_area = RectanglArea(points)
    rectangle_area.find_corners()
    rectangle_area.sort_points_area()
    #rectangle_area.print_points_area()
    return rectangle_area.get_biggest_area()


def part2(points: list[Position]) -> int:
    red_green_field = RedGreenField(points)
    red_green_field.find_red_green_field()
    rectangle_area = RectanglArea(points, red_green_field)
    
    rectangle_area.find_corners()
    rectangle_area.sort_points_area()
    #rectangle_area.print_points_area()
    
    # Plot points first, then overlay the rectangle
    plot_points(points)
    result = rectangle_area.find_first_inside()
    plt.show()  # Show the plot with both points and rectangle
    return result

def plot(points: list[Position]):
    """Plot points and show immediately."""
    plot_points(points)
    plt.show()

def plot_points(points: list[Position]):
    """Plot the points and connect them with lines (without showing)."""
    # Connect consecutive points with lines
    for i in range(len(points) - 1):
        plt.plot([points[i].col, points[i+1].col], [points[i].row, points[i+1].row], 'b-', alpha=0.5)
    # Connect last point to first point to close the polygon
    if len(points) > 2:
        plt.plot([points[-1].col, points[0].col], [points[-1].row, points[0].row], 'b-', alpha=0.5)
    # Scatter plot all points
    plt.scatter([p.col for p in points], [p.row for p in points], c='blue', s=50, zorder=3, label='Points')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Points and Rectangle')
    plt.legend()
    plt.grid(True, alpha=0.3)

def read_data(file: GetFile) -> list[list[int]]:
    return [Position(int(row[1]), int(row[0])) for row in file.get_row()]

def main():
    data_file = Path(__file__).parent / 'data/data.txt'
    file = GetFile(str(data_file), delimiter=',')
    points = read_data(file)
    
    #result1 = time_and_print("Part 1", part1, points)
    result2 = time_and_print("Part 2", part2, points)


if __name__ == "__main__":
    main()
