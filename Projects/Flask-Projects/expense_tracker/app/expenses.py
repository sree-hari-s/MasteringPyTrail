# expenses.py

from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.models import Expense
from app import db

# Function to log an expense
def log_expense(date, description, category, amount):
    user_id = session['user_id']
    new_expense = Expense(date=date, description=description, category=category, amount=amount, user_id=user_id)
    db.session.add(new_expense)
    db.session.commit()
    flash('Expense logged successfully.', 'success')

# Function to display monthly expense summary
def monthly_summary(month, year):
    user_id = session['user_id']
    expenses = Expense.query.filter_by(user_id=user_id).filter(db.text("strftime('%m', date) = :month AND strftime('%Y', date) = :year")).params(month=month, year=year).all()
    total_expense = sum(expense.amount for expense in expenses)
    flash(f"Total expenses for {month}/{year}: ${total_expense:.2f}", 'info')

# Function to display category-wise expense breakdown
def category_breakdown():
    user_id = session['user_id']
    categories = Expense.query.filter_by(user_id=user_id).with_entities(Expense.category).distinct()
    breakdown = {}
    for category in categories:
        category_expenses = Expense.query.filter_by(user_id=user_id, category=category[0]).all()
        total_expense = sum(expense.amount for expense in category_expenses)
        breakdown[category[0]] = total_expense
    flash(breakdown, 'info')
