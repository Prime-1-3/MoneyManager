import pytest
from tkinter import Tk  # Import Tkinter for creating a window
from FeedBack import Feedback

# Fixture to create an instance of Feedback with a Tkinter window
@pytest.fixture
def feedback_instance():
    window = Tk()
    feedback = Feedback(window)
    return feedback

# Test case to check if data is submitted when both income source and amount are provided
def test_submit_data_with_both_fields(feedback_instance):
    date = "2024-04-01"  # Example date
    income_source = "Salary"  # Example income source
    income_amount = "1000"  # Example income amount
    feedback_instance.submit_data(date, income_source, income_amount)
    # Assert that the warning label is set to "Successfully Submitted!!"
    assert feedback_instance.warning_label['text'] == "Successfully Submitted!!"

# Test case to check if warning label is displayed when income source is not provided
def test_submit_data_without_source(feedback_instance):
    date = "2024-04-01"  # Example date
    income_source = ""  # Empty income source
    income_amount = "1000"  # Example income amount
    feedback_instance.submit_data(date, income_source, income_amount)
    # Assert that the warning label is set to "Please Enter Income Source" and color is red
    assert feedback_instance.warning_label['text'] == "Please Enter Income Source"
    assert feedback_instance.warning_label['fg'] == "red"

# Test case to check if warning label is displayed when income amount is not provided
def test_submit_data_without_amount(feedback_instance):
    date = "2024-04-01"  # Example date
    income_source = "Salary"  # Example income source
    income_amount = ""  # Empty income amount
    feedback_instance.submit_data(date, income_source, income_amount)
    # Assert that the warning label is set to "Please Enter Income Amount" and color is red
    assert feedback_instance.warning_label['text'] == "Please Enter Income Amount"
    assert feedback_instance.warning_label['fg'] == "red"

# Test case to check if warning label is displayed when neither income source nor amount is provided
def test_submit_data_without_data(feedback_instance):
    date = "2024-04-01"  # Example date
    income_source = ""  # Empty income source
    income_amount = ""  # Empty income amount
    feedback_instance.submit_data(date, income_source, income_amount)
    # Assert that the warning label is set to "Please provide data in both field." and color is red
    assert feedback_instance.warning_label['text'] == "Please provide data in both field."
    assert feedback_instance.warning_label['fg'] == "red"

# Test case to check if warning label is displayed when income amount is not a numeric value
def test_submit_data_with_non_numeric_amount(feedback_instance):
    date = "2024-04-01"  # Example date
    income_source = "Salary"  # Example income source
    income_amount = "invalid"  # Non-numeric income amount
    feedback_instance.submit_data(date, income_source, income_amount)
    # Assert that the warning label is set to "Income Amount Can Be Only Positive Numbers" and color is red
    assert feedback_instance.warning_label['text'] == "Income Amount Can Be Only Positive Numbers"
    assert feedback_instance.warning_label['fg'] == "red"

# You can add more test cases as needed
