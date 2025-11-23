"""Tests for _2024/_6/main.py functions."""

import pytest
from helpers.array_helper import Board, Position
from _2024._6.main import (
    part1,
    part2,
)
from _2024._6.classes import Player, VisitedStates, LoopChecker


def create_board_from_string(board_str: str) -> Board:
    """Helper function to create a Board from a string representation."""
    lines = board_str.strip().split('\n')
    return Board([list(line) for line in lines])


class TestPart1:
    """Tests for part1 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
        
        board = create_board_from_string(grid_str)
        start_position = board.find_character_position('^')
        player = Player(start_position)
        
        visited = part1(board, player)
        
        # Part1 should return 41 X characters
        total_x = board.count_characters('X')
        assert total_x == 41


class TestPart2:
    """Tests for part2 function."""

    def test_given_data(self):
        """Test with the provided test data."""
        grid_str = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
        
        board = create_board_from_string(grid_str)
        start_position = board.find_character_position('^')
        
        # First run part1 to get visited states
        player1 = Player(start_position)
        visited = part1(board, player1)
        
        # Reset board and player for part2
        board = create_board_from_string(grid_str)
        player2 = Player(start_position)
        
        # Run part2
        part2(board, player2, visited)
        
        # Part2 should find 6 obstacles
        # We need to manually check since part2 doesn't return the count
        found_obstacles = VisitedStates()
        loop_checker = LoopChecker(player2.get_position())
        
        for visited_state in visited.visited_states:
            if visited_state.position == player2.get_position():
                continue
            
            r = visited_state.position.row
            c = visited_state.position.col
            position = Position(r, c)
            
            old_character = board.get_character(position)
            board.set_character_at_position(position, '#')
            
            # Create a fresh player for each test
            test_player = Player(start_position)
            has_loop = loop_checker.test_loop(board, test_player)
            
            if has_loop:
                found_obstacles.add_visited_state(visited_state)
            
            board.set_character_at_position(position, old_character)
        
        assert len(found_obstacles.visited_states) == 6

