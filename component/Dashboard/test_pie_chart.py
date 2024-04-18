#whether the  def draw_pie_charts(self) method takes data 
#randomly to draw pie chart
import pytest
from unittest.mock import MagicMock
from tkinter import Tk  # Import Tkinter's root window class

from body import Body

@pytest.fixture
def window():
    # Create a mock Tkinter root window for the test
    root = Tk()
    yield root  # Yield the root window to the test
    root.destroy()  # Destroy the root window after the test is complete

def test_draw_pie_charts_random_data(window):
    # Mock the Body instance
    body = Body(window)

    # Mock the file_handler.calculate_income_expenses() method to return specific data
    body.file_handler.calculate_income_expenses = MagicMock(return_value=({
        'Category1': 100,
        'Category2': 200,
        # Add more sample data here
    }, {
        'Category3': 150,
        'Category4': 250,
        # Add more sample data here
    }))

    # Call the method under test
    body.draw_pie_charts()

    # Add your assertions here based on the expected behavior of the method
    # For example, you might assert that certain canvas methods are called with expected arguments.
    # Or you might compare the output with expected values.
