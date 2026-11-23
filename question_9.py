"""
 grade(mark) returns the letter. It does not print. It uses the same bands as problem 5.
Pass: the 6 boundary calls match problem 5, and the function's return value is what the test checks.

Question 9
grade(mark) function
Logic / Breakdown
- Function ka naam grade hoga.
- Function ek mark receive karega.
- Same grading bands use hongi jo Question 5 mein use ki hain.
- Function grade ko return karega.
- Function ke andar print() nahi karna.
"""
# grade(mark) function marks receive kare aur grade return kare.

def grade(mark):

    # 80 ya above marks par A return hoga.
    if mark >= 80:
        return "A"

    # 65 se 79 marks par B return hoga.
    elif mark >= 65:
        return "B"

    # 50 se 64 marks par C return hoga.
    elif mark >= 50:
        return "C"

    # 50 se below marks par F return hoga.
    else:
        return "F"


# Function ko boundary values ke sath test kiya.
assert grade(49) == "F"
assert grade(50) == "C"
assert grade(64) == "C"
assert grade(65) == "B"
assert grade(79) == "B"
assert grade(80) == "A"

print("Grading system test with applying assertion of boundary values")
print("All grade tests passed")
