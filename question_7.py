"""
 Find the highest mark without max(). Include an all-negative list and a one-item list.
Pass: both cases are correct, and an empty list returns a clear message.

Logic / Breakdown
- Marks ki list banani hai.
- Agar list empty hai to clear message return karna hai.
- Pehle element ko highest mark maan lena hai.
- Loop mein har mark compare karna hai.
- Agar current mark highest se bara ho, to highest update karna hai.
"""
# Question 7
# max() use kiye baghair list ka highest mark find karo.

def find_highest_mark(marks):

    # Empty list mein highest mark nahi hota.
    if len(marks) == 0:
        return "List is empty"

    # Pehle mark ko highest maan kar start kiya.
    highest_mark = marks[0]

    # Har mark ko current highest ke sath compare kiya.
    for mark in marks:

        if mark > highest_mark:
            highest_mark = mark

    # Highest mark return kiya.
    return highest_mark


# Normal list test.
print("using simple list as a parameter of function",find_highest_mark([45, 78, 90, 66]))

# All-negative list test.
print("using negative elements list as a parameter of function",find_highest_mark([-10, -5, -20, -3]))

# One-item list test.
print("using signle element value list as a parameter of function",find_highest_mark([55]))

# Empty list test.
print("using empty list as a parameter of function",find_highest_mark([]))
