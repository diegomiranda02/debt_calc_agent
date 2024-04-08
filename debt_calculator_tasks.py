from crewai import Task
from textwrap import dedent

class CalculateDebtAmountTasks:
  
  def calculate_debt_amount(self, agent, debt_amount, days_late, daily_penalty_rate, penalty_cap, monthly_interest_rate):
    description = dedent("""
      **Task**: Calculate the total debt amount.
      
      **Details**:
      - **Debt Amount**: ${debt_amount}
      - **Days Late**: {days_late} days
      - **Daily Penalty Rate**: {daily_penalty_rate}%
      - **Penalty Cap**: ${penalty_cap}
      - **Monthly Interest Rate**: {monthly_interest_rate}%
      
      **Instructions**:
      Calculate the sum of the original debt amount, the accumulated penalty (capped by the penalty cap), and the accumulated interest. 
      Provide the final total debt amount as the result.
    """).format(debt_amount=debt_amount, days_late=days_late, daily_penalty_rate=daily_penalty_rate, penalty_cap=penalty_cap, monthly_interest_rate=monthly_interest_rate)

    expected_output = "The Total Amount Due"

    return Task(
      description=description,
      expected_output=expected_output,
      agent=agent
    )