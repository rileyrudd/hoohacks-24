import os, asyncio
from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


prompt = PromptTemplate(
        input_variables=["transaction_history"],
        template="""You are a financial expert for a banking company who is able to analyze one's personal monthly credit card statement and bank account statement. 
        By analyzing the following transaction history: {transaction_history}, provide a qualitative analysis of the user's financial health. 
        Focus on identifying patterns and trends in spending habits, without presenting any calculated numbers. 
        Offer insights that highlight areas for potential improvement.  
        Formulate a clear and actionable recommendation for the user to strengthen their financial health in the upcoming month.
        You will only respond in JSON format with three keys and no leading or trailing characters:
        * "insights" (string): A detailed analysis highlighting key observations and trends without calculations.
        * "financial health" (string): A rating of the user's financial health ("very bad", "bad", "moderate", "good", or "very good").
        * "recommendation" (string): A specific and actionable recommendation for improving financial health. Provide some examples from the transaction history if there is a scope of optimization of expenses. 
        """
    )


prompt_chat = PromptTemplate(
        input_variables=["transaction_history","question"],
        template="""You are a financial expert for a banking company who is able to analyze one's personal monthly credit card statement and bank account statement. 
        By analyzing the following transaction history: {transaction_history}, advise the user on the following {question}. 
        You will only respond in JSON format with one key and no leading or trailing characters:
        * "advice" (string): A summarized recommendation with a qualitative reasoning highlighting key observations and without calculations.Formulate a clear and actionable recommendation for the user to help user make decisions.  
        """
    )

transaction_history=[
  { "type": "credit_card", "date": "2023-09-01", "description": "Grocery Store", "amount": 150.00, "balance": 2850.00 },
  { "type": "credit_card", "date": "2023-09-03", "description": "Restaurant Dinner", "amount": 50.00, "balance": 2800.00 },
  { "type": "credit_card", "date": "2023-09-10", "description": "Gas Station", "amount": 40.00, "balance": 2760.00 },
  { "type": "credit_card", "date": "2023-09-15", "description": "Utility Bill Payment", "amount": 100.00, "balance": 2660.00 },
  { "type": "credit_card", "date": "2023-09-20", "description": "Salary Deposit", "amount": 3000.00, "balance": 5660.00 },
  { "type": "credit_card", "date": "2023-09-25", "description": "Online Shopping", "amount": 200.00, "balance": 5460.00 },
  { "type": "credit_card", "date": "2023-09-30", "description": "Investment Portfolio Contribution", "amount": 500.00, "balance": 4960.00 },
  
  { "type": "bank", "date": "2023-08-01", "description": "Rent Payment", "amount": 1200.00, "balance": 2800.00 },
  { "type": "bank", "date": "2023-08-05", "description": "Grocery Store", "amount": 200.00, "balance": 2600.00 },
  { "type": "bank", "date": "2023-08-12", "description": "Internet and Cable Bill", "amount": 80.00, "balance": 2520.00 },
  { "type": "bank", "date": "2023-08-15", "description": "Freelance Gig Income", "amount": 700.00, "balance": 3220.00 },
  { "type": "bank", "date": "2023-08-21", "description": "Dinner with Friends", "amount": 80.00,  "balance": 3140.00 },
  { "type": "bank", "date": "2023-08-25", "description": "Savings Account Transfer", "amount": 300.00, "balance": 3440.00 },
  { "type": "bank", "date": "2023-08-29", "description": "Online Shopping", "amount": 150.00, "balance": 3290.00 }
]

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# repo_id = "meta-llama/Llama-2-7b"


llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.9, token="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"
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

llm_chat = LLMChain(prompt=prompt_chat, llm=llm)

def get_analysis():
    return llm_chain.run(transaction_history)


def get_response(question:str):
    return llm_chat.run(transaction_history=transaction_history, question=question)

# def langchain_agent():
#     tools = load_tools(["llm-math"], llm=llm)
#     agent = initialize_agent(tools, llm, prompt)
#     agent.run(transaction_history=transaction_history)

