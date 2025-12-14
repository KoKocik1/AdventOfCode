import unittest
from pathlib import Path
from helpers import GetFile, Position
from _2025._9.classes import RedGreenField, RectanglArea

class TestPart2(unittest.TestCase):
    
    def test_test2_txt(self):
        """Test dla test2.txt - powinien znaleźć prostokąt o powierzchni 77"""
        data_file = Path(__file__).parent / 'data/test2.txt'
        file = GetFile(str(data_file), delimiter=',')
        points = [Position(int(row[1]), int(row[0])) for row in file.get_row()]
        
        red_green_field = RedGreenField(points)
        red_green_field.find_red_green_field()
        rectangle_area = RectanglArea(points, red_green_field)
        
        rectangle_area.find_corners()
        rectangle_area.sort_points_area()
        
        result = rectangle_area.find_first_inside()
        
        self.assertEqual(result, 77, f"Oczekiwano 77, otrzymano {result}")
        
        # Sprawdź czy znaleziony prostokąt to (0,0) do (10,6)
        # Powierzchnia = (10-0+1) * (6-0+1) = 11 * 7 = 77

if __name__ == '__main__':
    unittest.main()

