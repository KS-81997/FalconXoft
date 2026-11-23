"""
A program averages a list and crashes on an empty list with ZeroDivisionError. Handle it with a clear result. Do not hide the error in a bare except.
Pass: the empty list prints a message, and a normal list still returns the average.
Logic / Breakdown
- Function list receive karega.
- Agar list empty hai to division nahi karni.
- Empty list par clear message return karna hai.
- Normal list par sum calculate karna hai.
- Sum ko list ki length se divide karke average return karna hai.
- except use karne ke bajaye pehle condition check karni hai.

Empty list ki length zero hoti hai. Jab program total / len(numbers) karta hai to 0 / 0 hota hai, jo ZeroDivisionError raise karta hai.

Question 11
"""
# Empty list ki average calculate karte waqt ZeroDivisionError handle karo.

def calculate_average(numbers):

    # Empty list mein division possible nahi hoti.
    if len(numbers) == 0:
        return "Cannot calculate average of an empty list"

    # List ke tamam numbers ka sum calculate kiya.
    total = sum(numbers)

    # Total ko list ki length se divide karke average nikala.
    average = total / len(numbers)

    return average


# Empty list test.
empty_result = calculate_average([])

if isinstance(empty_result, str):
    print(empty_result)
else:
    print("Average:", empty_result)


# Normal list test.
normal_result = calculate_average([10, 20, 30, 40])

print("Average:", normal_result)

# Function ke return values ko assert se test kiya.
print("testing the empty list error and not empty list execution ")
assert calculate_average([]) == "Cannot calculate average of an empty list"
assert calculate_average([10, 20, 30, 40]) == 25

print("All average tests passed")
