import tkinter as tk

class MoneyManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Manager")

        # Create and configure the main frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Add components to the main frame
        self.label = tk.Label(self.main_frame, text="Money Manager", font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.add_expense_button = tk.Button(self.main_frame, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack(pady=10)

        self.view_transactions_button = tk.Button(self.main_frame, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Quit", command=root.destroy)
        self.quit_button.pack(pady=10)

    def add_expense(self):
        # Add logic for handling "Add Expense" button click
        print("Add Expense button clicked")

    def view_transactions(self):
        # Add logic for handling "View Transactions" button click
        print("View Transactions button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyManagerApp(root)
    root.mainloop()
