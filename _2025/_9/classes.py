from ast import Pass
from helpers.array_helper import Position, BoardArray
from _2025._5.classes import Range, RangeHelper
import matplotlib.pyplot as plt
class RedGreenField:
    points: list[Position]
    all_points: list[Position]
    col_set: dict[int, list[tuple[int, int]]]
    row_set: dict[int, list[tuple[int, int]]]
    col_all_points: dict[int, list[Position]]
    row_all_points: dict[int, list[Position]]
    min_rows: dict[int, int]
    max_rows: dict[int, int]
    min_cols: dict[int, int]
    max_cols: dict[int, int]
    
    def __init__(self, points: list[Position]):
        self.points = points
        self.all_points = []
        self.col_set = {}
        self.row_set = {}
        self.col_all_points = {}
        self.row_all_points = {}
        self.min_rows = {}
        self.max_rows = {}
        self.min_cols = {}
        self.max_cols = {}
    
    def _check_col_set(self, point: Position) -> bool:
        if point.row in self.col_set:
            for start_col, end_col in self.col_set[point.row]:
                if start_col <= point.row <= end_col:
                    return True
        return False
    
    def _check_row_set(self, point: Position) -> bool:
        if point.col in self.row_set:
            for start_row, end_row in self.row_set[point.col]:
                if start_row <= point.col <= end_row:
                    return True
        return False

    
    def is_inside(self, ranges: list[tuple[str, Range, Range]]) -> bool:
        for range in ranges:
            if range[0] == 'COL':
                if not self.is_range_inside_col((range[1], range[2])):
                    return False
            elif range[0] == 'ROW':
                if not self.is_range_inside_row((range[1], range[2])):
                    return False
        return True
    
    
    def add_point_to_set_col(self, point: Position, point1: Position):
        if point.row not in self.row_set:
            self.row_set[point.row] = []
        self.row_set[point.row].append((point.col, point1.col))
    
    def add_point_to_set_row(self, point: Position, point1: Position):
        if point.col not in self.col_set:
            self.col_set[point.col] = []
        self.col_set[point.col].append((point.row, point1.row))
        
        
    def find_red_green_field(self):
        
        for idx in range(len(self.points)):
            point = self.points[idx]
            if idx + 1 < len(self.points):
                next_point = self.points[idx + 1]
            else:
                next_point = self.points[0]
            
            if point.row not in self.min_rows:
                self.min_rows[point.row] = point.row
            if point.row not in self.max_rows:
                self.max_rows[point.row] = point.row
            if point.col not in self.min_cols:
                self.min_cols[point.col] = point.col
            if point.col not in self.max_cols:
                self.max_cols[point.col] = point.col
            
            if point.row < self.min_rows[point.row]:
               self.min_rows[point.row] = point.row
            if point.row > self.max_rows[point.row]:
                self.max_rows[point.row] = point.row
            if point.col < self.min_cols[point.col]:
                self.min_cols[point.col] = point.col
            if point.col > self.max_cols[point.col]:
                self.max_cols[point.col] = point.col
            

            if point.row == next_point.row:
                for col in range(min(point.col, next_point.col), max(point.col, next_point.col) + 1):
                    if col == 3141:
                        pass
                    self.all_points.append(Position(point.row, col))
                if point.row not in self.col_all_points:
                    self.col_all_points[point.row] = set()
                self.col_all_points[point.row].add(Range(
                    point.col,
                    next_point.col))

            elif point.col == next_point.col:
                if point.col == 3141:
                    pass
                for row in range(min(point.row, next_point.row), max(point.row, next_point.row) + 1):
                    self.all_points.append(Position(row, point.col))
                if point.col not in self.row_all_points:
                    self.row_all_points[point.col] = set()
                self.row_all_points[point.col].add(Range(
                    point.row, next_point.row))

        
        # First logic for row_all_points
        for col, rows in self.row_all_points.items():
            optimized = RangeHelper.optimize_ranges(rows)
            optimized.sort(key=lambda x: x.start)    
            self.row_all_points[col] = optimized

                        
        # Second logic for col_all_points
        for row, cols in self.col_all_points.items():
            optimized = RangeHelper.optimize_ranges(cols)
            optimized.sort(key=lambda x: x.start)
            self.col_all_points[row] = optimized
            
        #prepare a plot from col_all_points
        # for row, cols in self.col_all_points.items():
        #     for col in cols:
                
        #         plt.plot([col.start, col.end], [row, row],  'b-', linewidth=1)
        # plt.show()
        
        # for col, rows in self.row_all_points.items():
        #     for row in rows:
        #         plt.plot([col, col], [row.start, row.end],  'b-', linewidth=1)
        # plt.show()



    def is_range_inside_col(self, range_tuple: tuple[Range, Range]) -> bool:

        range_to_check = range_tuple[0]
        # if range_to_check.end - range_to_check.start < 2:
        #     return True
        
        range_to_iterate = range_tuple[1]
        for r in range(range_to_iterate.start+1, range_to_iterate.end):
            if r in self.row_all_points:
                for p in self.row_all_points[r]:
                    if p.is_range_inside_range(range_to_check):
                        return False
        return True

    def is_range_inside_row(self, range_tuple: tuple[Range, Range]) -> bool:
        range_to_check = range_tuple[0]
        # if range_to_check.end - range_to_check.start < 2:
        #     return True
        
        range_to_iterate = range_tuple[1]
        for r in range(range_to_iterate.start+1, range_to_iterate.end):
            if r in self.col_all_points:
                for p in self.col_all_points[r]:
                    if p.is_range_inside_range(range_to_check):
                        return False
        return True



class Rectangle:
    one_corner: Position
    other_corner: Position
    
    def __init__(self, one_corner: Position, other_corner: Position= None):
        self.one_corner = one_corner
        self.other_corner = other_corner

    def get_area(self, other_corner: Position= None) -> int:
        if other_corner is None:
            if self.other_corner is None:
                return 0
            else:
                other_corner = self.other_corner
        return (abs(self.one_corner.row - other_corner.row) + 1) * (abs(self.one_corner.col - other_corner.col) + 1)

    def __str__(self) -> str:
        return f"Rectangle(c1={self.one_corner}, c2={self.other_corner})"
    
    def __repr__(self) -> str:
        return f"Rectangle(c1={self.one_corner}, c2={self.other_corner})"
    
class RectanglArea:
    points: list[Position]
    points_area: dict[Rectangle, int]
    red_green_field: RedGreenField
    
    def __init__(self, points: list[Position], red_green_field: RedGreenField = None):
        self.points = points
        self.points_area = {}
        self.red_green_field = red_green_field
    
    def find_corners(self):

        for idx, point in enumerate(self.points):
            
            for other in self.points[idx+1:]:
                if point != other:
                    act_rectangle = Rectangle(point)
                    area = act_rectangle.get_area(other)
                    # if area > best_area:
                    #     best_area = area
                    #     best_point = other
                    act_rectangle.other_corner = other
                    self.points_area[act_rectangle] = area
    
    def find_first_inside(self):

        for rect, area in self.points_area:

            point=rect.one_corner
            other=rect.other_corner
            
            min_col = min(point.col, other.col)
            max_col = max(point.col, other.col)
            min_row = min(point.row, other.row)
            max_row = max(point.row, other.row)
            
            if point and other:
                range_a = ('COL', Range(min_row, max_row), Range(min_col, max_col))
                range_b = ('ROW', Range(min_col, max_col), Range(min_row, max_row))
                
                if self.red_green_field.is_inside([range_a, range_b]):
                    test=self.red_green_field.is_inside([range_a, range_b])
                    self._plot_rectangle(rect)
                    return area
        return -1
    
    def _plot_rectangle(self, rect: Rectangle):
        """Plot a rectangle showing all 4 corners connected on the current plot."""
        point = rect.other_corner
        other = rect.one_corner
        
        # Get all 4 corners of the rectangle (ordered to form a closed rectangle)
        corners = [
            Position(point.row, point.col),      # Corner 1
            Position(point.row, other.col),      # Corner 2
            Position(other.row, other.col),       # Corner 3
            Position(other.row, point.col),      # Corner 4
            Position(point.row, point.col)        # Close the rectangle
        ]
        
        # Plot rectangle outline
        corner_cols = [c.col for c in corners]
        corner_rows = [c.row for c in corners]
        plt.plot(corner_cols, corner_rows, 'r-', linewidth=3, label='Found Rectangle', zorder=4)
        
        # Highlight corners with squares
        plt.scatter(corner_cols[:-1], corner_rows[:-1], c='red', s=150, zorder=5, marker='s', edgecolors='darkred', linewidths=2)
        
        # Update legend (don't show here - let main.py handle it)
        plt.legend()
    
    def sort_points_area(self):
        self.points_area = sorted(self.points_area.items(), key=lambda item: item[1], reverse=True)
    
    def get_biggest_area(self) -> int:
        print(f"Biggest area: {self.points_area[0]}")
        return self.points_area[0][1]
    
    def print_points_area(self):
        for rectangle, area in self.points_area:
            print(f"{rectangle}: {area}")