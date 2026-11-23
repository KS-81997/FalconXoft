"""
Store price and quantity for 3 shop items and print the total. 
Every name describes the value (price_rice, not a).
Pass: the total matches a hand calculation.
Arithmetic and money
"""
"""
Logic / Breakdown
- 3 items ki price aur quantity store karni hai.
- Har item ka total price = price × quantity.
- Teeno item totals ko add karna hai.
- Meaningful variable names use karne hain.
"""
#Solution question 2
price_rice = 250
quantity_rice = 2

price_sugar = 180
quantity_sugar = 3

price_oil = 550
quantity_oil = 1

# Har item ki total cost calculate ki.
total_rice = price_rice * quantity_rice
total_sugar = price_sugar * quantity_sugar
total_oil = price_oil * quantity_oil

# Teeno items ki cost add karke final bill nikala.
total_bill = total_rice + total_sugar + total_oil

print("Rice total:", total_rice)
print("Sugar total:", total_sugar)
print("Oil total:", total_oil)
print("Total bill:", total_bill)

