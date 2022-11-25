loan_amount = int(input("What is the total amount borrowed? "))
apr = int(input("What is the annual percentage rate? "))
num_years = int(input("How many years? "))

for i in range(num_years):
  loan_amount += loan_amount * (apr / 100)
rounded_total = round(loan_amount, 2)
print(f"You will owe ${rounded_total} after {num_years} years paying on the loan.")