# ------------------------------------------------------------------------------------------------- #
# Title: Assignment 08 Test Processing Classes Module
# # Description: Test harness to test processing classes
# ChangeLog: (Who, When, What)
# JZhang,6/16/2025,Created Script
# ------------------------------------------------------------------------------------------------- #
import json
import tempfile
import unittest

from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.student_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2025-06-16", "ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2025-06-16", "ReviewRating": 4},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name)

    def test_write_data_to_file(self):
        # Create some sample employee objects
        sample_employee = [
            Employee("John", "Doe", "2025-06-16", 3),
            Employee("Alice", "Smith", "2025-06-16", 4),
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employee)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employee))
        self.assertEqual(file_data[0]["FirstName"], "John")
        self.assertEqual(file_data[1]["ReviewRating"], 4)

if __name__ == "__main__":
    unittest.main()



