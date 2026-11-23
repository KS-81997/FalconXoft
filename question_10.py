"""
Split the bill into subtotal, discount, tax, and total. Each function is tested on its own.
Pass: each function passes alone, and total matches problem 3.

Question 10

Bill ko 4 separate functions mein divide karna hai:
1. calculate_subtotal() items ki prices add karega.
2. calculate_discount() subtotal ka discount calculate karega.
3. calculate_tax() discounted amount par tax calculate karega.
4. calculate_total() final bill return karega.
Har function apna result return karega, print nahi karega
"""
# Bill ko subtotal, discount, tax aur total functions mein split karo.

def calculate_subtotal(items):
    # Items ki tamam prices add karke subtotal return kiya.
    subtotal = 0

    for item_price in items:
        subtotal = subtotal + item_price

    return subtotal


def calculate_discount(subtotal):
    # Subtotal ka 10% discount calculate kiya.
    discount = subtotal * 10 / 100

    return discount


def calculate_tax(amount_after_discount):
    # Discount ke baad amount par 17% tax calculate kiya.
    tax = amount_after_discount * 17 / 100

    return tax


def calculate_total(items):
    # Pehle subtotal function call kiya.
    subtotal = calculate_subtotal(items)

    # Subtotal ka discount calculate kiya.
    discount = calculate_discount(subtotal)

    # Discount minus karke remaining amount nikala.
    discounted_amount = subtotal - discount

    # Discounted amount par tax calculate kiya.
    tax = calculate_tax(discounted_amount)

    # Final amount return kiya.
    total = discounted_amount + tax

    return round(total)


# 5 items ki prices.
items = [1000, 500, 250, 750, 300]

# Har function ko separately test kiya.
assert calculate_subtotal(items) == 2800
assert calculate_discount(2800) == 280
assert calculate_tax(2520) == 428.4
assert calculate_total(items) == 2948

print("Subtotal test with boundary value :", calculate_subtotal(items))
print("Discount test with boundary value:", calculate_discount(2800))
print("Tax test with boundary value:", calculate_tax(2520))
print("Total test with boundary value:", calculate_total(items))

print("All bill tests passed")
