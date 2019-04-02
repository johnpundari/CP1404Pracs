"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $ "))
if sales < 1000:
    bonus = 0.10 * sales
    print("Bonus: $", bonus)
else:
    bonus = 0.15 * sales
print("Bonus: $", bonus)
