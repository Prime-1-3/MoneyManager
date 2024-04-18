import pytest
from tkinter import Tk
from FeedBack import Feedback  # Assuming the class is in a module named feedback


@pytest.fixture
def feedback_instance():
    root = Tk()
    feedback = Feedback(root)
    return feedback


def test_submit_data_with_valid_input(feedback_instance):
    feedback_instance.submit_data("Mar 08 2023", 'Groceries', '50')
   
  