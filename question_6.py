"""
Electricity bill: first 100 units at Rs 10, next 100 at Rs 15, the rest at Rs 25. Test 0, 100, 101, 200, and 350 units.
Pass: all 5 amounts match a hand total.
Logic / Breakdown

Electricity bill progressive slabs mein calculate hoga:
- First 100 units: Rs 10 per unit.
- Next 100 units: Rs 15 per unit.
- Remaining units: Rs 25 per unit.
Agar units 150 hain, to pehle 100 units ka rate Rs 10 aur remaining 50 units ka rate Rs 15 hoga.
"""
# Question 6
# Electricity units ke according progressive bill calculate karo.

units = 350

# Bill ko zero se start kiya.
bill = 0

# First 100 units ka rate Rs 10 hai.
if units <= 100:
    bill = units * 10

# 101 se 200 units tak pehle 100 units Rs 10
# aur remaining units Rs 15 par calculate hongi.
elif units <= 200:
    bill = (100 * 10) + ((units - 100) * 15)

# 200 se above units par first 200 ka bill
# aur remaining units Rs 25 par calculate hongi.
else:
    bill = (
        (100 * 10)
        + (100 * 15)
        + ((units - 200) * 25)
    )

print("Electricity bill:", bill)
print("Electricity bill managment system with different usage criteria!")


# Assignment ke test cases.
test_units = [0, 100, 101, 200, 350]

for units in test_units:

    if units <= 100:
        bill = units * 10
    elif units <= 200:
        bill = (100 * 10) + ((units - 100) * 15)
    else:
        bill = (
            (100 * 10)
            + (100 * 15)
            + ((units - 200) * 25)
        )

    print(units, "units =", bill, "rupees")
