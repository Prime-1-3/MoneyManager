# testing def calculate_income_expenses(self): method 
#where if the method can take income and expense data or not,
#where income data is indicated if flag=1 and expense data is indicated if flag =0,
# and finally if the method Keep the top 4 categories for both expenses and income and sum the rest for "Others"

import os
from pathlib import Path
import csv
import pytest
from file_handling import FileHandling
data_path = Path(__file__).parent.parent.parent / "data_store" / "data.csv"
@pytest.fixture
def file_handling_instance():
    # Assuming you need a file instance to test the method
    return FileHandling()

def test_calculate_income_expenses(file_handling_instance):
    # Mocking the data.csv file
    file_handling_instance.filename = data_path

    # Call the method under test
    top_income, top_expenses = file_handling_instance.calculate_income_expenses()

    # Write your assertions based on the expected behavior of the method
    # Example assertions:
    assert isinstance(top_income, dict)
    assert isinstance(top_expenses, dict)
    assert len(top_income) <= 5  # Including 'Others', there should be at most 5 categories
    assert len(top_expenses) <= 5  # Including 'Others', there should be at most 5 categories
    assert 'Others' in top_income  # 'Others' category should be present in top_income
    assert 'Others' in top_expenses  # 'Others' category should be present in top_expenses
    # Add more assertions based on your specific requirements and expectations
    # ...

class FileHandling:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.filename = self.OUTPUT_PATH / Path("data_store/data.csv")

    def calculate_income_expenses(self):
        income_data = {}
        expenses_data = {}

        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flag = int(row['flag'])
                source = row['Source']
                amount = float(row['Amount'])

                if flag == 0:  # Expense
                    expenses_data[source] = amount
                elif flag == 1:  # Income
                    income_data[source] = amount

        # Sort the dictionaries by value in descending order
        sorted_income_data = dict(sorted(income_data.items(), key=lambda item: item[1], reverse=True))
        sorted_expenses_data = dict(sorted(expenses_data.items(), key=lambda item: item[1], reverse=True))

        # Keep the top 4 categories for expenses and sum the rest for "Others"
        top_expenses = dict(list(sorted_expenses_data.items())[:4])
        other_expenses = sum(list(sorted_expenses_data.values())[4:])
        top_expenses['Others'] = other_expenses

        # Keep the top 4 categories for income and sum the rest for "Others"
        top_income = dict(list(sorted_income_data.items())[:4])
        other_income = sum(list(sorted_income_data.values())[4:])
        top_income['Others'] = other_income

        return top_income, top_expenses
