#Grade a mark: A from 80, B from 65, C from 50, F below 50. Test 49, 50, 64, 65, 79, and 80.
#Pass: all 6 boundaries are correct.
# Question:4
"""
Logic / Breakdown
- Marks 80 ya above hon to A.
- Marks 65 ya above hon to B.
- Marks 50 ya above hon to C.
- 50 se below hon to F.
- Conditions highest marks se lowest marks ki taraf check karni hain
"""
# Student ke marks ke according grade calculate karo.

marks = 79

# Pehle highest grade check kiya.
if marks >= 80:
    grade = "A"

# Agar A nahi hai to B ki condition check hogi.
elif marks >= 65:
    grade = "B"

# Agar B bhi nahi hai to C check hoga.
elif marks >= 50:
    grade = "C"

# 50 se kam marks par student fail hai.
else:
    grade = "F"

print("Grade:", grade)

print("Grading system with boundaries!")


# Assignment ke boundary test cases.
test_marks = [49, 50, 64, 65, 79, 80]

for mark in test_marks:

    if mark >= 80:
        grade = "A"
    elif mark >= 65:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"
    print(mark, "=", grade)
