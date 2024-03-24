import os
import json
import predictionguard as pg
from langchain import PromptTemplate

os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

prompt = PromptTemplate(
        input_variables=["transaction_history"],
        template="""You are a financial expert who is able to analyze one's personal monthly credit card statement and bank account statement. 
        By analyzing the following transaction history: {transaction_history} give a deep analysis on what went good, what went wrong, 
        and recommend some actionable items to improve one's personal financial health.
        Only use the factual information from the transaction history to answer the question.
        You can only return the response in JSON format with 3 keys: 
        "financial health" is the rating of one's financial condition based on the analysis provided.
        "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in theupcoming month.
        "analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
        Total response should be under 900 characters.
        """,
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

result = pg.Completion.create(
    model="Neural-Chat-7B",
    prompt=prompt.format(transaction_history=transaction_history)
)
	  
print(len(result['choices'][0]['text']))

# messages = [
#     {
#         "role": "system",
#         "content": """You are a financial expert who is able to analyze one's personal monthly credit card statement, bank account statement, and cash
# expense log, and give a deep analysis on what went good, what went wrong, and recommend some actionable items to improve one's personal financial health
# You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good",
# "very good"), and "recommendation" (string).
# "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the upcoming month.
# "analysis" consists of the in-depth analysis and statistics summary that is important for the user to know about their personal financial condition.
# "financial health" is the rating of one's financial condition based on the analysis provided. Total response should be under 900 characters.

# Let's start!"""
#     },
#     {
#         "role": "user",
#         "content": transaction_history
#     }
# ]

# result = pg.Chat.create(
#     model="Yi-34B-Chat",
#     messages=messages
# )

# print(json.dumps(
#     result,
#     sort_keys=True,
#     indent=4,
#     separators=(',', ': ')
# ))
