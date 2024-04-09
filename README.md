# AI Crew: Debt Amount Calculator
## Introduction
This project showcases the power of CrewAI framework to calculate debt amounts considering various factors like days late, daily penalty rate, penalty cap, and monthly interest rate.

By [@diegomiranda02](https://linkedin.com/in/diego-miranda-de-paula/)

## CrewAI Framework

CrewAI makes it easy to collaborate with AI agents. In this example, it was implemented an agent to be an expert in calculating payment delay interest rates in contracts.

## Running the Script
- **Install Dependencies**: Run `poetry install --no-root`.
- **Execute the Script**: Run `poetry run python main.py` and input the debt amount, the days of payment delayed, the daily penalty rate, the penalty cap and monthly interest rate

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from crewai import Agent
from langchain_community.llms import Ollama

from tools.debt_calculator import DebtCalculatorTools

class FinanceDepartmentAgents():
  
  ollama_openhermes = Ollama(model="openhermes")
 
  def debt_calculator_agent(self):
    return Agent(
      role='Debt Calculator Expert',
      goal='Calculate the debt amount due based on the accumulated penalty and the accumulated interest',
      backstory='An expert in calculating the debt amount due based on the accumulated penalty and the accumulated interest',
      tools=[
                DebtCalculatorTools.calculate_debt
            ],
      llm=self.ollama_openhermes,
      max_iter=3,
      verbose=True
    )
```

## License
This project is released under the MIT License. Feel free to explore, modify, and share! 🚀📊

