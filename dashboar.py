import tkinter as tk

class MoneyManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Money Manager")
        
        # Create and pack widgets
        self.label_balance = tk.Label(self, text="Balance: $0.00")
        self.label_balance.pack(pady=10)
        
        self.button_income = tk.Button(self, text="Add Income", command=self.add_income)
        self.button_income.pack(pady=5)
        
        self.button_expense = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.button_expense.pack(pady=5)
        
        self.text_summary = tk.Text(self, height=10, width=40)
        self.text_summary.pack(pady=10)
        
        self.update_balance()

    def add_income(self):
        income_amount = float(input("Enter income amount: "))
        # Add income processing logic here
        self.update_balance()

    def add_expense(self):
        expense_amount = float(input("Enter expense amount: "))
        # Add expense processing logic here
        self.update_balance()

    def update_balance(self):
        # Retrieve balance from backend or database
        # For now, just setting it to a fixed value
        balance = 1000.00
        self.label_balance.config(text=f"Balance: ${balance:.2f}")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MoneyManagerApp()
    app.run()
