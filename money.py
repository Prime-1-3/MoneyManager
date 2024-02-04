import os
from datetime import datetime

def record_expense(amount, category, date, data_file):
    with open(data_file, 'a') as file:
        file.write(f'{amount},{category},{date}\n')

def calculate_summary(data_file):
    total_expense = 0
    categories = {}

    with open(data_file, 'r') as file:
        for line in file:
            amount, category, _ = line.strip().split(',')
            amount = float(amount)

            total_expense += amount

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\nMonthly Expense Summary:")
    print(f"Total Expense: ${total_expense:.2f}\n")

    for category, amount in categories.items():
        print(f"{category.capitalize()}: ${amount:.2f}")

def main():
    data_file = 'expenses.txt'

    while True:
        print("\n1. Record Expense")
        print("2. View Monthly Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            date = datetime.now().strftime('%Y-%m-%d')
            record_expense(amount, category, date, data_file)
            print("Expense recorded successfully!")

        elif choice == '2':
            calculate_summary(data_file)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
