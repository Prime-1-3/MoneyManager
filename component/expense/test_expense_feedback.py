import pytest
from tkinter import Tk
from FeedBack import Feedback  # Assuming the class is in a module named feedback


@pytest.fixture
def feedback_instance():
    root = Tk()
    feedback = Feedback(root)
    return feedback


def test_submit_data_with_valid_input(feedback_instance):
    feedback_instance.submit_data('2024-04-01', 'Groceries', '50')
    # You may need to add assertions here based on the behavior of your application
    # For example, you can assert that the warning label is not shown


def test_submit_data_with_missing_source(feedback_instance):
    feedback_instance.submit_data('2024-04-01', '', '50')
    # You can assert that the "Please Enter Expense Reason" warning label is shown


def test_submit_data_with_missing_amount(feedback_instance):
    feedback_instance.submit_data('2024-04-01', 'Groceries', '')
    # You can assert that the "Please Enter Expense Amount" warning label is shown


def test_submit_data_with_missing_data(feedback_instance):
    feedback_instance.submit_data('2024-04-01', '', '')
    # You can assert that the "Please provide data in both fields" warning label is shown


def test_submit_data_with_non_numeric_amount(feedback_instance):
    feedback_instance.submit_data('2024-04-01', 'Groceries', 'abc')
    # You can assert that the "Expense Amount Can Be Only Positive Numbers" warning label is shown


# Add more test cases as needed
