# ------------------------------------------------------------------------------- #
# Title: Assignment 08 Test Processing Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# JZhang,6.16.2025,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setup(self):
        self.employee_type = []

    def test_input_menu_choice(self):
        # Simulate user input '1' and check if the function returns '1'
        with patch('builtins.input', return_value='1'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '1')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['John', 'Doe', '2025-06-16', 3]):
            IO.input_employee_data(self.employee_type)
            self.assertEqual(len(self.employee_type), 1)
            self.assertEqual(self.employee_type[0].first_name, 'John')
            self.assertEqual(self.employee_type[0].last_name, 'Doe')
            self.assertEqual(self.employee_type[0].review_date, '2025-06-16')
            self.assertEqual(self.employee_type[0].review_rating, 3)

        # Simulate invalid rating (must be 1 through 5)
        with patch('builtins.input', side_effect=['Alice', 'Smith', 'invalid', 6]):
            IO.input_employee_data(self.employee_type)
            self.assertEqual(len(self.employee_type), 1)  # Data should not be added due to invalid input


if __name__ == "__main__":
    unittest.main()
