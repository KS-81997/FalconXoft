"""
Question 8
Logic / Breakdown
- Deposits positive values hongi.
- Withdrawals negative values hongi.
- Starting balance zero hoga.
- Har day transaction ko balance mein add karna hai.
- Running balance print karna hai.
- Pehli baar balance negative ho to day number save karna hai.
- Agar balance kabhi negative nahi hota to clear message show karna hai.
"""
# Monthly deposits aur withdrawals ka running balance calculate karo.

transactions = [1000, -200, 500, -1800, 300, -100]

# Starting balance zero rakha.
balance = 0

# Abhi tak negative balance ka day nahi mila.
first_negative_day = None

# Har transaction ek day ko represent karti hai.
for day, transaction in enumerate(transactions, start=1):

    # Aaj ki transaction balance mein add ki.
    balance = balance + transaction

    print("Day", day, "Transaction:", transaction,
          "Balance:", balance)

    # Sirf pehli baar negative hone ka day save kiya.
    if balance < 0 and first_negative_day is None:
        first_negative_day = day

# Agar balance negative hua tha to day show karo.
if first_negative_day is not None:
    print("First negative balance day:", first_negative_day)

# Agar kabhi negative nahi hua to clear message.
else:
    print("Balance never went negative")


# History jo kabhi negative nahi hoti.
safe_transactions = [1000, -200, 500, -300, 200]

balance = 0
first_negative_day = None

for day, transaction in enumerate(safe_transactions, start=1):

    balance = balance + transaction

    print("Day", day, "Balance:", balance)

    if balance < 0 and first_negative_day is None:
        first_negative_day = day

if first_negative_day is not None:
    print("First negative balance day when balance goes to negative :", first_negative_day)
else:
    print("Balance never went negative when balance not goes to negative")
 