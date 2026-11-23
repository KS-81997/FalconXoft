"""Arithmetic and Money
Question 3: Discount aur sales tax
Logic / Breakdown
- 5 items ki prices store karni hain.
- Sab prices add karke subtotal banana hai.
- Pehle 10% discount apply karna hai.
- Discount ke baad 17% tax apply karna hai.
- Same bill par pehle tax aur phir discount bhi calculate karna hai.
- Dono totals compare karne hain.
"""

# Question 3:
# 5 items par 10% discount aur 17% sales tax calculate karo.

# Store 5 items prices
item_1 = 1000
item_2 = 500
item_3 = 250
item_4 = 750
item_5 = 300

# Sab items ki prices add karke subtotal banaya.
subtotal = item_1 + item_2 + item_3 + item_4 + item_5
print("subtotal value",subtotal)
# Pehle 10% discount calculate kiya.
discount = subtotal * 10 / 100
print("discount ",discount)
# Subtotal mein se discount minus kiya.
discounted_bill = subtotal - discount
print("discounted_bill",discounted_bill)

# Discount ke baad 17% tax calculate kiya.
tax = discounted_bill * 17 / 100
print("after discount 17% tax applied",tax)
# Discount ke baad tax add karke final bill banaya.
discount_then_tax = round(discounted_bill + tax)
print("Discount + tax bill",discount_then_tax)
# Ab pehle original subtotal par 17% tax calculate kiya.
tax_before_discount = subtotal * 17 / 100
print("tax applied before discount on a subtotal amount",tax_before_discount)

# Tax ko original bill mein add kiya.
bill_after_tax = subtotal + tax_before_discount
print("sum of subtotal and tax applied on before discounted amount",bill_after_tax)

# Original subtotal ka 10% discount calculate kiya.
discount_after_tax = subtotal * 10 / 100
print("discount after tax",discount_after_tax)

# Tax-inclusive bill mein se discount minus kiya.
tax_then_discount = round(bill_after_tax - discount_after_tax)


# Results display kiye.
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Discount then tax:", discount_then_tax)
print("Tax then discount:", tax_then_discount)
