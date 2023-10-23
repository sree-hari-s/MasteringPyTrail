from datetime import datetime
import sqlite3

# Database initialization
conn = sqlite3.connect("expense_tracker.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    description TEXT,
    category TEXT,
    amount REAL
)''')

# Function to log an expense
def log_expense(date, description, category, amount):
    cursor.execute("INSERT INTO expenses (date, description, category, amount) VALUES (?, ?, ?, ?)", (date, description, category, amount))
    conn.commit()

# Function to display monthly expense summary
def monthly_summary(month, year):
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?", (month, year))
    result = cursor.fetchone()
    total_expense = result[0] if result[0] else 0.0
    print(f"Total expenses for {month}/{year}: ${total_expense:.2f}")

# Function to display category-wise expense breakdown
def category_breakdown():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    results = cursor.fetchall()
    for category, total in results:
        print(f"{category}: ${total:.2f}")

# Main program loop
while True:
    print("Expense Tracker Menu:")
    print("1. Log an Expense")
    print("2. Monthly Expense Summary")
    print("3. Category-wise Expense Breakdown")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        description = input("Enter a description: ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        log_expense(date, description, category, amount)
        print("Expense logged successfully.")

    elif choice == "2":
        month = input("Enter the month (MM): ")
        year = input("Enter the year (YYYY): ")
        monthly_summary(month, year)

    elif choice == "3":
        category_breakdown()

    elif choice == "4":
        print("Exiting Expense Tracker.")
        conn.close()
        break

    else:
        print("Invalid choice. Please select a valid option.")
