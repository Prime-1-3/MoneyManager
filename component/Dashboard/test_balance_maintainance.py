import pytest
from refactor_show_info import ShowInfo

@pytest.fixture
def show_info_instance():
    # Mock the FileHandling object or use a fixture to provide a sample data file
    return ShowInfo(window=None)

def test_total_balance_calculation(show_info_instance):
    # Mock the data for income and expenses to test the calculation
    show_info_instance.data.calculate_income_expenses = lambda: ({'income1': 100, 'income2': 200}, {'expense1': 50, 'expense2': 75})
    
    # Update balance labels
    show_info_instance.update_balance_labels()

    # Check if total balance is calculated correctly
    assert show_info_instance.total_balance == 175  # (100 + 200) - (50 + 75) = 275 - 125 = 175
