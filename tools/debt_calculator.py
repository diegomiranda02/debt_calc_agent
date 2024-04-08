from langchain_community.tools import tool


class DebtCalculatorTools():

    def __init__(self, task_manager):
        self.task_manager = task_manager

    @tool("Calculates the total amount due for a debt, considering the debt_amount, the accumulated interest and the accumulated penalty")
    def calculate_total_amount_for_a_debt(self, debt_amount, accumulated_interest, accumulated_penalty):
        """Useful to calculate the total amount due for a debt, considering both the accumulated interest and the accumulated penalty"""

        task_name = "calculate_total_amount_for_a_debt"

        if self.task_manager.should_execute(task_name):

            print('###################################################################')
            print('Debt information')
            print(debt_amount)
            print(accumulated_interest)
            print(accumulated_penalty)
            print('###################################################################')

            total_amount = debt_amount + accumulated_penalty + accumulated_interest

            self.task_manager.update_status(task_name, True)

            return total_amount
        
        else:
            return f"Task '{task_name}' already executed or not required."
    
    @tool("Calculate the accumulated penalty for a debt, considering days late, the daily penalty rate and the penalty cap")
    def calculate_accumulated_penalty_for_a_debt(self, debt_amount, days_late, daily_penalty_rate, penalty_cap):
        """Useful to calculate the accumulated penalty for a debt, considering days late, the daily penalty rate and the penalty cap"""

        task_name = "calculate_accumulated_penalty_for_a_debt"

        if self.task_manager.should_execute(task_name):

            penalty_limit = debt_amount * penalty_cap
            accumulated_penalty = min(days_late * daily_penalty_rate * debt_amount, penalty_limit)

            self.task_manager.update_status(task_name, True)

            return accumulated_penalty

        else:
            return f"Task '{task_name}' already executed or not required."
    
    @tool("Calculate the accumulated interest for a debt, considering the debt amount, the number of days late and the monthly interest rate")
    def calculate_accumulated_interest_for_a_debt(self, debt_amount, days_late, monthly_interest_rate):
        """Useful to calculate the accumulated interest for a debt, considering the debt amount, the number of days late and the monthly interest rate"""

        task_name = "calculate_accumulated_interest_for_a_debt"

        if self.task_manager.should_execute(task_name):

            daily_interest = (monthly_interest_rate * debt_amount) / 30
            accumulated_interest = days_late * daily_interest

            self.task_manager.update_status(task_name, True)

            return accumulated_interest
        
        else:
            return f"Task '{task_name}' already executed or not required."