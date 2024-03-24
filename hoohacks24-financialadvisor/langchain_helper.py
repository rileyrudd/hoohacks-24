import os
import json
import predictionguard as pg
from langchain import PromptTemplate

os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

# prompt = PromptTemplate(
#         input_variables=["transaction_history"],
#         template="""You are a financial expert who is able to analyze one's personal monthly credit card statement and bank account statement. 
#         By analyzing the following transaction history: {transaction_history} give a deep analysis on what went good, what went wrong, 
#         and recommend some actionable items to improve one's personal financial health.
#         Only use the factual information from the transaction history to answer the question.
#         You can only return the response in JSON format with 3 keys: "analysis" (string), "financial health" ("very bad", "bad", "moderate", "good", "very good"), and "recommendation" (string).
#         "financial health" is the rating of one's financial condition based on the analysis provided.
#         "recommendation" is the final recommendation that the advisor will give to the user so that they can improve their financial health in the
#         upcoming month.
#         """,
#     )

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

#         If you cannot draw valuable insights from the given data or you don't have enough information to answer the question, say "Feels like I don't have enough information to comment at the moment".

# transaction_history="""
# ##
# Monthly Credit Card Statement
 
# Date: 2023-09-01
# Description: Grocery Store
# Amount: $150.00
# Balance: $2,850.00
 
# Date: 2023-09-03
# Description: Restaurant Dinner
# Amount: $50.00
# Balance: $2,800.00
 
# Date: 2023-09-10
# Description: Gas Station
# Amount: $40.00
# Balance: $2,760.00
 
# Date: 2023-09-15
# Description: Utility Bill Payment
# Amount: $100.00
# Balance: $2,660.00
 
# Date: 2023-09-20
# Description: Salary Deposit
# Amount: $3,000.00
# Balance: $5,660.00
 
# Date: 2023-09-25
# Description: Online Shopping
# Amount: $200.00
# Balance: $5,460.00
 
# Date: 2023-09-30
# Description: Investment Portfolio Contribution
# Amount: $500.00
# Balance: $4,960.00
 
# ##
# Bank Account Statement
 
# Date: 2023-08-01
# Description: Rent Payment
# Amount: $1,200.00
# Balance: $2,800.00
 
# Date: 2023-08-05
# Description: Grocery Store
# Amount: $200.00
# Balance: $2,600.00
 
# Date: 2023-08-12
# Description: Internet and Cable Bill
# Amount: $80.00
# Balance: $2,520.00
 
# Date: 2023-08-15
# Description: Freelance Gig Income
# Amount: $700.00
# Balance: $3,220.00
 
# Date: 2023-08-21
# Description: Dinner with Friends
# Amount: $80.00
# Balance: $3,140.00
 
# Date: 2023-08-25
# Description: Savings Account Transfer
# Amount: $300.00
# Balance: $3,440.00
 
# Date: 2023-08-29
# Description: Online Shopping
# Amount: $150.00
# Balance: $3,290.00
 
# ##
# Cash Expense Log
 
# Date: 2023-07-03
# Description: Coffee Shop
# Amount: $5.00
# Balance: $95.00
 
# Date: 2023-07-10
# Description: Movie Tickets
# Amount: $20.00
# Balance: $75.00
 
# Date: 2023-07-18
# Description: Gym Membership
# Amount: $50.00
# Balance: $25.00
 
# Date: 2023-07-22
# Description: Taxi Fare
# Amount: $30.00
# Balance: -$5.00 (Negative balance indicates a debt)
 
# Date: 2023-07-28
# Description: Bookstore
# Amount: $40.00
# Balance: -$45.00
 
# Date: 2023-07-30
# Description: Cash Withdrawal
# Amount: $100.00
# Balance: -$145.00
  
# """

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
