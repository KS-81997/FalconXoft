#Ask for a birth year and print the age this year. Run it for 3 years the mentor picks.

#Pass: the ages are correct, and you can say why input() must be turned into a number.
#Why input() must be converted?

#input() string return karta hai. Agar hum string ke sath mathematical subtraction karenge to error aayega. 
#Is liye int() use karke birth year ko number banate hain.

# Question 1:
# Birth year input lo aur current year se age calculate karo.

current_year = 2026

# input() text deta hai, is liye birth year ko integer mein convert kiya.
birth_year = int(input("Enter your birth year: "))

# Current year mein se birth year minus karke age nikali.
age = current_year - birth_year

print("Your age is:", age)

# Hardcoded birth years 
birth_year_1 = 2000
birth_year_2 = 2005
birth_year_3 = 1998

print("Age of person 1:", current_year - birth_year_1)
print("Age of person 2:", current_year - birth_year_2)
print("Age of person 3:", current_year - birth_year_3)
