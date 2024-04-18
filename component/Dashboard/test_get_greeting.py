#  whether the def get_greeting(self) method shows greeting message according to  the time where the time format is " current_hour < 12: "Good Morning",
            #12 <= current_hour < 18: "Good Afternoon",
            #18 <= current_hour < 24: "Good Evening"



import pytest
from datetime import datetime
from header import Header

class TestHeader:
    @pytest.fixture
    def header_instance(self):
        # Assuming you have a window object to pass to Header constructor
        window = None  # Replace None with your window object
        return Header(window)

    def test_get_greeting_morning(self, header_instance, mocker):
        mocker.patch.object(header_instance, 'get_time', return_value='08:00')
        assert header_instance.get_greeting() == "Good Morning"

    def test_get_greeting_afternoon(self, header_instance, mocker):
        mocker.patch.object(header_instance, 'get_time', return_value='14:00')
        assert header_instance.get_greeting() == "Good Afternoon"

    def test_get_greeting_evening(self, header_instance, mocker):
        mocker.patch.object(header_instance, 'get_time', return_value='20:00')
        assert header_instance.get_greeting() == "Good Evening"

    # Add more test cases if needed


