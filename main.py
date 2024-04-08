from crewai import Crew
from textwrap import dedent
from debt_calculator_tasks import CalculateDebtAmountTasks
from finance_department_agents import FinanceDepartmentAgents
from task_manager import TaskManager


class FinanceDepartmentCrew:

  def __init__(self, debt_amount, days_late, daily_penalty_rate, penalty_cap, monthly_interest_rate):
    # Convert string inputs to floats for mathematical operations
    self.debt_amount = float(debt_amount)
    self.days_late = int(days_late)
    self.daily_penalty_rate = float(daily_penalty_rate)
    self.penalty_cap = float(penalty_cap)
    self.monthly_interest_rate = float(monthly_interest_rate)
    
  def run(self):

    task_manager = TaskManager()
    agents = FinanceDepartmentAgents(task_manager=task_manager)
    tasks = CalculateDebtAmountTasks()

    debt_calculator_agent = agents.debt_calculator_agent()
    
    calculate_debt_amount_task = tasks.calculate_debt_amount(
      agent = debt_calculator_agent,
      debt_amount = self.debt_amount, 
      days_late = self.days_late, 
      daily_penalty_rate = self.daily_penalty_rate, 
      penalty_cap = self.penalty_cap, 
      monthly_interest_rate = self.monthly_interest_rate
    )
    
    financeDepartmentCrew = Crew(
      agents=[
        debt_calculator_agent
      ],
      tasks=[calculate_debt_amount_task]
    )

    result = financeDepartmentCrew.kickoff()
    return result

if __name__ == "__main__":
    print("## Total Debt Amount Calculator")
    print('-------------------------------')

    # Input gathering
    debt_amount = input(dedent("""What is the debt amount? """))
    days_late = input(dedent("""How many days is the payment delayed? """))
    daily_penalty_rate = input(dedent("""What is the delay penalty rate? """))
    penalty_cap = input(dedent("""What is the penalty cap? """))
    monthly_interest_rate = input(dedent("""What is the monthly interest rate? """))
    
    # Initialize and run the FinanceDepartmentCrew
    finance_department_crew = FinanceDepartmentCrew(debt_amount, days_late, daily_penalty_rate, penalty_cap, monthly_interest_rate)
    result = finance_department_crew.run()
    print("\n\n########################")
    print("## Here is the total debt amount")
    print("########################\n")
    print(result)