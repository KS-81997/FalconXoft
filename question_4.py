"""
print(0.1 + 0.2) shows a long float. Build the same bill in paisa (integers) so the receipt never shows that error.

Pass: 3 bills match to the paisa, and the float line is explained in one sentence."""
"""
Logic / Breakdown
- Decimal prices ko paisay mein convert karna hai.
- 1 paisa = 100 paisay.
- paisay integer mein store honge.
- Discount aur tax integer arithmetic se calculate karenge.
- Receipt par final amount rupees mein show karenge.
Float issue explanation:
0.1 + 0.2 ka result exactly 0.3 nahi hota, kyun ke computer binary floating-point mein kuch decimal values ko exact store nahi kar sakta.
Note: // integer division karta hai, is liye paisay calculate karte waqt fractional paisay discard ho sakte hain.
 Real financial systems mein rounding policy carefully define karni hoti hai.
 """

# Question 4:
# Prices rupees mein hain, inko paisay mein convert kiya.
product_1_paisa = 1000 * 100
product_2_paisa = 500 * 100
product_3_paisa = 250 * 100
product_4_paisa = 750 * 100
product_5_paisa = 300 * 100

# Integer values add karke subtotal nikala.
subtotal_paisa = (
    product_1_paisa
    + product_2_paisa
    + product_3_paisa
    + product_4_paisa
    + product_5_paisa
)

# 10% discount integer paisay mein calculate kiya.
discount_paisa = subtotal_paisa * 10 // 100
discounted_paisa = subtotal_paisa - discount_paisa

# 17% tax discount ke baad calculate kiya.
tax_paisa = discounted_paisa * 17 // 100

# Final amount paisay mein calculate kiya.
total_paisa = discounted_paisa + tax_paisa

# Receipt par rupees aur paisay alag show kiye.
rupees = total_paisa // 100
paisa = total_paisa % 100

print("Total:", rupees, "rupees and", paisa, "paisa")
