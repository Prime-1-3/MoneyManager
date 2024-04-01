import csv
from datetime import datetime

import pytest
from DataManager import DataManager  # Import the DataManager class from your module

# Define a fixture to create an instance of DataManager with a sample CSV file
@pytest.fixture
def sample_instance():
    # Assuming your CSV file is named 'sample_data.csv'
    instance = DataManager('data.csv')
    return instance

# Test case to check if the data is sorted correctly by date
def test_data_sorted_by_date(sample_instance):
    data = sample_instance.get_data()
    dates = [datetime.strptime(row[1], "%b %d %Y") for row in data[1:]]
    assert dates == sorted(dates)

# Test case to check if the summary of source and amount according to date is correct
def test_summary_by_date(sample_instance):
    data = sample_instance.get_data()
    summary = {}
    for row in data[1:]:
        date_string = row[1]
        source = row[2]
        amount = float(row[3])
        date = datetime.strptime(date_string, "%b %d %Y").date()
        if date not in summary:
            summary[date] = {}
        if source not in summary[date]:
            summary[date][source] = 0
        summary[date][source] += amount
    
    # Assert summary correctness using sample assertions
    assert summary[datetime(2024, 2, 27).date()] == {'tuition': 3000.0, 'loan': 1000.0}
    assert summary[datetime(2024, 3, 4).date()] == {'shopping': 1000.0, 'scholarship': 5000.0}

# Add more test cases as needed
