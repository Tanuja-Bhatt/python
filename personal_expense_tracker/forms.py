from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, DateField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length, Email, NumberRange, DataRequired
from datetime import date


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(), 
        Length(min=4, max=25)
    ])
    email = StringField('Email', validators=[
        InputRequired(), 
        Email(), 
        Length(min=6, max=100)
    ])
    password = PasswordField('Password', validators=[
        InputRequired(), 
        Length(min=6, max=100)
    ])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class ExpenseForm(FlaskForm):
    amount = DecimalField('Amount', validators=[
        InputRequired(), 
        NumberRange(min=0.01, message="Amount must be greater than 0")
    ])
    category = SelectField('Category', choices=[
        ('food', 'Food & Dining'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('healthcare', 'Healthcare'),
        ('shopping', 'Shopping'),
        ('education', 'Education'),
        ('other', 'Other')
    ], validators=[InputRequired()])
    date = DateField('Date', validators=[InputRequired()], default=date.today)
    description = TextAreaField('Description', validators=[Length(max=200)])
    submit = SubmitField('Add Expense')


class BudgetForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('food', 'Food & Dining'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('healthcare', 'Healthcare'),
        ('shopping', 'Shopping'),
        ('education', 'Education'),
        ('other', 'Other')
    ], validators=[InputRequired()])
    limit_amount = DecimalField('Budget Limit', validators=[
        InputRequired(), 
        NumberRange(min=0.01, message="Budget must be greater than 0")
    ])
    start_date = DateField('Start Date', validators=[InputRequired()])
    end_date = DateField('End Date', validators=[InputRequired()])
    submit = SubmitField('Set Budget')
