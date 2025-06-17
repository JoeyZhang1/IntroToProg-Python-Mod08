# ------------------------------------------------------------------------------------------------- #
# Title: Assignment 08 Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# JZhang,6/16/2025,Created Script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Person
from data_classes import Employee

def test_person_class():
    # Test person class
    print("Testing person class:")

    person = Person("John", "Doe")
    print(person) # Should print John Doe

    try:
        # Try to set an invalid first name
        person.first_name = "123"
    except ValueError as e:
        print(f"error: {e}")

    try:
        # Try to set an invalid last name
        person.last_name = "456"
    except ValueError as e:
        print(f"error: {e}")

def test_employee_class():

    # Test Employee class
    print("\nTesting Employee class:")
    employee = Employee("Alice", "Smith", "2025-12-03", 4)
    print(employee)  # Should print "Alice, Smith, 2025-12-03, 4"

    try:
        # Try to set an invalid rating
        employee.review_rating = "Rating"
    except ValueError as e:
        print(f"Error: {e}")  # Should print "Error: GPA must be a numeric value."


# Run the test cases
test_person_class()
test_employee_class()





