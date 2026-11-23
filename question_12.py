"""
A small CLI asks for a quantity. abc and -3 are rejected and the prompt repeats. A positive integer is accepted.
Pass: both bad inputs never crash, and 4 is accepted.

Question 12
Logic / Breakdown
- User se quantity input leni hai.
- Input ko integer mein convert karna hai.
- Agar user abc enter kare to ValueError aayega.
- Agar quantity zero ya negative ho to reject karna hai.
- Invalid input par prompt repeat karna hai.
- Positive integer accept karke loop stop karna hai.
"""

# Quantity input lo, invalid values reject karo aur prompt repeat karo.

while True:

    # User se quantity input li.
    quantity_input = input("Enter quantity: ")

    try:
        # Input ko integer mein convert kiya.
        quantity = int(quantity_input)

        # Quantity positive honi chahiye.
        if quantity <= 0:
            print("Quantity must be a positive number")
            continue

        # Positive quantity mil gayi, loop stop kar diya.
        print("Accepted quantity:", quantity)
        break

    except ValueError:
        # Agar input integer nahi hai to user ko message diya.
        print("Invalid input. Please enter a whole number.")
