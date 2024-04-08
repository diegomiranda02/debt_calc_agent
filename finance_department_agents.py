from crewai import Agent
from langchain_community.llms import Ollama

from tools.debt_calculator import DebtCalculatorTools

class FinanceDepartmentAgents():
  
  def __init__(self, task_manager):
        self.ollama_openhermes = Ollama(model="openhermes")
        self.debt_calculator_tools = DebtCalculatorTools(task_manager)

  def debt_calculator_agent(self):
    return Agent(
      role='Debt Calculator Expert',
      goal='Calculate the debt amount due based on the accumulated penalty and the accumulated interest',
      backstory='An expert in calculating the payment delay interest rate in a contract',
      tools=[
                self.debt_calculator_tools.calculate_accumulated_penalty_for_a_debt,
                self.debt_calculator_tools.calculate_accumulated_interest_for_a_debt,
                self.debt_calculator_tools.calculate_total_amount_for_a_debt,
            ],
        llm=self.ollama_openhermes,
        verbose=True
    )