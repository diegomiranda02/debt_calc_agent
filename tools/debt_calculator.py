
from langchain_community.tools import tool

class DebtCalculatorTools:    

    @tool("Calculates the total amount due for a debt by considering the original debt amount, days late, daily penalty rate, penalty cap, and the monthly interest rate")
    def calculate_debt(debt_amount, days_late, daily_penalty_rate, penalty_cap, monthly_interest_rate):
        """This tool calculates the total debt amount by considering the original debt amount,
        days late, daily penalty rate, penalty cap, and monthly interest rate.
        It encompasses calculating the accumulated interest, accumulated penalty, and summing up to find the total debt amount."""

        # Calculate accumulated penalty
        penalty_limit = debt_amount * penalty_cap
        accumulated_penalty = min(days_late * daily_penalty_rate * debt_amount, penalty_limit)

        # Calculate accumulated interest
        daily_interest = (monthly_interest_rate * debt_amount) / 30
        accumulated_interest = days_late * daily_interest

        # Calculate total amount due
        total_amount = debt_amount + accumulated_penalty + accumulated_interest

        # Optionally print the detailed breakdown
        print('###################################################################')
        print('Debt calculation breakdown:')
        print(f'Debt Amount: {debt_amount}')
        print(f'Accumulated Penalty: {accumulated_penalty}')
        print(f'Accumulated Interest: {accumulated_interest}')
        print(f'Total Amount Due: {total_amount}')
        print('###################################################################')
 
        return total_amount