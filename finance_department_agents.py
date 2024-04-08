from crewai import Agent
from langchain_community.llms import Ollama

from tools.debt_calculator import DebtCalculatorTools

class FinanceDepartmentAgents():
  
  ollama_openhermes = Ollama(model="openhermes")
 
  def debt_calculator_agent(self):
    return Agent(
      role='Debt Calculator Expert',
      goal='Calculate the debt amount due based on the accumulated penalty and the accumulated interest',
      backstory='An expert in calculating the payment delay interest rate in a contract',
      tools=[
                DebtCalculatorTools.calculate_debt
            ],
      llm=self.ollama_openhermes,
      max_iter=3,
      verbose=True
    )