import pytest
from tkinter import Tk
import tkinter
from FeedBack import Feedback  


@pytest.fixture
def feedback_instance():
    root = Tk()
    feedback = Feedback(root)
    return feedback


def test_submit_data_with_valid_input(feedback_instance):
    feedback_instance.update_balance_labels()

    assert feedback_instance.total_balance == "successful"
