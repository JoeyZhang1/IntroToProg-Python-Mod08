# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-processing classes
# # Description: A collection of processing classes for managing the application
# ChangeLog: (Who, When, What)
# JZhang,6/8/2025,Created Script
# JZhang 6/16/2025,Modified Script
# ------------------------------------------------------------------------------------------------- #

# Import the json module
import json
import data_classes as data
import presentation_classes as pres

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JZhang,6.8.2025,Created Class
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        JZhang,6.8.2025,Created function

        :param file_name: string data with name of file to read from
        :return: list
        """
        employee_data_list = []
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_type = data.Employee()
                    employee_type.first_name=employee["FirstName"]
                    employee_type.last_name=employee["LastName"]
                    employee_type.review_date=employee["ReviewDate"]
                    employee_type.review_rating=employee["ReviewRating"]
                    employee_data_list.append(employee_type)
        except FileNotFoundError as e:
            pres.IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            pres.IO.output_error_messages("There was a non-specific error!", e)
        return employee_data_list

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        JZhang,6.8.2025,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=4)
        except TypeError as e:
            pres.IO.output_error_messages("Please check that the data is a valid JSON format")
        except PermissionError as e:
            pres.IO.output_error_messages("Please check the data file's read/write permission")
        except Exception as e:
            pres.IO.output_error_messages("There was a non-specific error!")