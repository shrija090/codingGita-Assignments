
# ============================================================
# ASSIGNMENT 3 — OPERATORS, STRINGS, INPUT & OUTPUT
# ============================================================


# ============================================================
# Q1 — COMPARISON OPERATORS
# ============================================================

a = 15
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# Output:
# True
# False
# False
# True
# True
# False


# ============================================================
# Q2 — COMPARE EXPRESSIONS
# ============================================================

x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)

# Output:
# True
# False
# False
# True
# True


# ============================================================
# Q3 — COMPARISON WITH ARITHMETIC
# ============================================================

a = 10
b = 5

print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)

# Output:
# True
# True
# False
# True


# ============================================================
# Q4 — STRING COMPARISON
# ============================================================

print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")

# Output:
# True
# False
# True

# Strings are case-sensitive.
# "Python" and "python" are different.


# ============================================================
# Q5 — ASSIGNMENT OPERATORS
# ============================================================

x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x)

# Values:
# 20 -> 30 -> 25 -> 50 -> 10


# ============================================================
# Q6 — ASSIGNMENT OPERATOR PRACTICE
# ============================================================

marks = 50

marks += 10
marks -= 5
marks *= 2

print(marks)

# Output:
# 110


# ============================================================
# Q7 — BASIC MEMBERSHIP
# ============================================================

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)

# Output:
# True
# False
# False


# ============================================================
# Q8 — CHARACTER MEMBERSHIP
# ============================================================

word = "computer"

print("p" in word)
print("x" in word)
print("c" not in word)

# Output:
# True
# False
# False


# ============================================================
# Q9 — CASE SENSITIVITY IN MEMBERSHIP
# ============================================================

text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)

# Output:
# True
# False
# True
# False


# ============================================================
# Q10 — MEMBERSHIP WITH USER INPUT
# ============================================================

text = input("Enter a word or sentence: ")

print("a" in text)


# ============================================================
# Q11 — EMAIL SYMBOL CHECK
# ============================================================

email = input("Enter an email address: ")

print("@" in email)


# ============================================================
# Q12 — FIND CHARACTER CODES
# ============================================================

print(ord("A"))
print(ord("a"))
print(ord("Z"))
print(ord("z"))
print(ord("0"))
print(ord("9"))
print(ord("@"))

# Output:
# 65
# 97
# 90
# 122
# 48
# 57
# 64


# ============================================================
# Q13 — CONVERT CODES TO CHARACTERS
# ============================================================

print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(48))
print(chr(57))
print(chr(64))

# Output:
# A
# B
# a
# b
# 0
# 9
# @


# ============================================================
# Q14 — UPPERCASE AND LOWERCASE
# ============================================================

print(ord("A"))
print(ord("a"))
print(ord("B"))
print(ord("b"))

# Answers:
# ord("A") = 65
# ord("a") = 97
# ord("B") = 66
# ord("b") = 98
# ord("a") is larger than ord("A")
# Difference = 32
# Difference between B and b = 32


# ============================================================
# Q15 — CHARACTER CODE PROGRAM
# ============================================================

character = input("Enter a character: ")

print(ord(character))


# ============================================================
# Q16 — NEXT CHARACTER
# ============================================================

character = input("Enter an uppercase letter: ")

print(chr(ord(character) + 1))


# ============================================================
# Q17 — CHARACTER COMPARISON AND UNICODE
# ============================================================

print("A" < "B")
print("a" < "b")
print("A" < "a")
print("0" < "9")

# Output:
# True
# True
# True
# True


# ============================================================
# Q18 — UNICODE CHARACTER CHALLENGE
# ============================================================

print(chr(9731))
print(chr(9829))
print(chr(8377))

# Output:
# ☃
# ♥
# ₹

# Verification:
print(ord("☃"))
print(ord("♥"))
print(ord("₹"))

# Output:
# 9731
# 9829
# 8377


# ============================================================
# Q19 — BASIC INDEXING
# ============================================================

text = "PYTHON"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])

# Output:
# P
# Y
# N
# O


# ============================================================
# Q20 — POSITIVE AND NEGATIVE INDEXING
# ============================================================

text = "COMPUTER"

print(text[0])
print(text[3])
print(text[-1])
print(text[-3])

# Output:
# C
# P
# R
# E


# ============================================================
# Q21 — PREDICT THE OUTPUT
# ============================================================

text = "PYTHON"

print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

# Output:
# P
# T
# N
# O


# ============================================================
# Q22 — INDEXING USER INPUT
# ============================================================

word = input("Enter a word: ")

print(word[0])
print(word[-1])


# ============================================================
# Q23 — THINK CAREFULLY ABOUT INDEXING
# ============================================================

word = "PROGRAM"

print(word[0])
print(word[2])
print(word[-1])
print(word[-4])

# Output:
# P
# O
# M
# R


# ============================================================
# Q24 — BASIC SLICING
# ============================================================

text = "PYTHON"

print(text[0:3])
print(text[2:5])
print(text[1:6])

# Output:
# PYT
# THO
# YTHON


# ============================================================
# Q25 — START AND STOP
# ============================================================

text = "PROGRAMMING"

print(text[:4])
print(text[4:])
print(text[:])

# Output:
# PROG
# RAMMING
# PROGRAMMING


# ============================================================
# Q26 — NEGATIVE SLICING
# ============================================================

text = "COMPUTER"

print(text[-5:])
print(text[:-3])
print(text[-6:-2])

# Output:
# PUTER
# COMPU
# OMPU


# ============================================================
# Q27 — STEP IN SLICING
# ============================================================

text = "PYTHON"

print(text[::2])
print(text[1::2])
print(text[::-1])

# Output:
# PTO
# YHN
# NOHTYP


# ============================================================
# Q28 — REVERSE A STRING
# ============================================================

text = input("Enter a string: ")

print(text[::-1])


# ============================================================
# Q29 — ALTERNATE CHARACTERS
# ============================================================

text = input("Enter a string: ")

print(text[::2])


# ============================================================
# Q30 — FIRST AND LAST THREE CHARACTERS
# ============================================================

text = input("Enter a string: ")

print(text[:3])
print(text[-3:])


# ============================================================
# Q31 — SLICING CHALLENGE
# ============================================================

text = "ABCDEFGHIJ"

print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])

# Output:
# CEG
# IGE
# JHFDB

# text[2:8:2]
# start = 2
# stop = 8
# step = 2

# text[8:2:-2]
# start = 8
# stop = 2
# step = -2

# text[::-2]
# start = default
# stop = default
# step = -2


# ============================================================
# Q32 — BTECH-CSE-2026
# ============================================================

text = "BTECH-CSE-2026"

print(text[:5])
print(text[6:9])
print(text[10:])

# Output:
# BTECH
# CSE
# 2026


# ============================================================
# Q33 — BASIC split()
# ============================================================

text = "Python is easy"

print(text.split())

# Output:
# ['Python', 'is', 'easy']


# ============================================================
# Q34 — CUSTOM SEPARATOR
# ============================================================

data = "apple,banana,mango"

print(data.split(","))

# Output:
# ['apple', 'banana', 'mango']


# ============================================================
# Q35 — SEPARATOR NOT PRESENT
# ============================================================

text = "Python is easy"

print(text.split(","))

# Output:
# ['Python is easy']


# ============================================================
# Q36 — SPLIT A FULL NAME
# ============================================================

name = input("Enter full name: ")

words = name.split()

print(words[0])
print(words[1])
print(words[2])


# ============================================================
# Q37 — MULTIPLE INPUTS USING split()
# ============================================================

first_name, last_name = input(
    "Enter first name and last name: "
).split()

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")


# ============================================================
# Q38 — THREE NUMERIC INPUTS
# ============================================================

a, b, c = input("Enter three numbers: ").split()

a = int(a)
b = int(b)
c = int(c)

print(a + b + c)


# ============================================================
# Q39 — STUDENT RECORD
# ============================================================

data = input("Enter student record: ")

name, age, course, city = data.split(",")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"City: {city}")


# ============================================================
# Q40 — EMAIL ANALYZER
# ============================================================

email = input("Enter email: ")

username, domain = email.split("@")

print(f"Username: {username}")
print(f"Domain: {domain}")


# ============================================================
# Q41 — SENTENCE ANALYZER
# ============================================================

sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Total number of words: {len(words)}")


# ============================================================
# Q42 — NEW LINE
# ============================================================

print("Hello\nWorld")


# ============================================================
# Q43 — TAB
# ============================================================

print("Name:\tRahul")
print("Age:\t20")
print("City:\tAhmedabad")


# ============================================================
# Q44 — BACKSLASH
# ============================================================

print("C:\\Python\\Programs")


# ============================================================
# Q45 — SINGLE QUOTE
# ============================================================

print("It's Python")


# ============================================================
# Q46 — DOUBLE QUOTE
# ============================================================

print('He said "Hello"')


# ============================================================
# Q47 — PREDICT THE OUTPUT
# ============================================================

print("Python\nProgramming")

# Output:
# Python
# Programming


# ============================================================
# Q48 — COMBINED ESCAPE SEQUENCES
# ============================================================

print("Student Details\n")
print("Name:\tRahul")
print("Age:\t20")
print("Course:\tB.Tech")


# ============================================================
# Q49 — sep
# ============================================================

print("2026", "09", "09", sep="-")

# Output:
# 2026-09-09


# ============================================================
# Q50 — end
# ============================================================

print("Hello", end=" ")
print("Python")

# Output:
# Hello Python


# ============================================================
# Q51 — sep AND end
# ============================================================

print("10", "20", "30", sep="-")
print("40", "50", "60", sep="-")

# Output:
# 10-20-30
# 40-50-60


# ============================================================
# Q52 — STUDENT INTRODUCTION
# ============================================================

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
course = input("Enter course: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course: {course}")


# ============================================================
# Q53 — FORMATTED PRICE
# ============================================================

price = float(input("Enter price: "))

print(f"{price:.2f}")


# ============================================================
# Q54 — STRING AND INTEGER
# ============================================================

age = int(input("Enter age: "))

print("Age after 5 years:", age + 5)


# ============================================================
# Q55 — INCORRECT QUOTES
# ============================================================

print("It's Python")


# ============================================================
# Q56 — INCORRECT SLICING SYNTAX
# ============================================================

text = "Python"

print(text[1:4])


# ============================================================
# Q57 — INCORRECT split() SEPARATOR
# ============================================================

# Input:
# 10 20

a, b = input().split()

print(a)
print(b)


# ============================================================
# Q58 — STRING ADDITION VS NUMERIC ADDITION
# ============================================================

a, b = input("Enter two numbers: ").split()

a = int(a)
b = int(b)

print(a + b)


# ============================================================
# Q59 — ESCAPE SEQUENCE DEBUGGING
# ============================================================

print("C:\\new\\test")


# ============================================================
# Q60 — STUDENT RESULT INFORMATION
# ============================================================

name = input("Enter student name: ")

marks = input("Enter three marks: ").split()

mark1 = int(marks[0])
mark2 = int(marks[1])
mark3 = int(marks[2])

total = mark1 + mark2 + mark3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")


# ============================================================
# Q61 — STUDENT ID ANALYZER
# ============================================================

student_id = input("Enter student ID: ")

parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]

last_three = student_id[-3:]

roll_number = int(roll_number)

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll_number}")


# ============================================================
# Q62 — USERNAME GENERATOR
# ============================================================

full_name = input("Enter full name: ")

parts = full_name.split()

first_name = parts[0]
last_name = parts[-1]

username = first_name.lower() + "." + last_name.lower()

print(username)


# ============================================================
# Q63 — SENTENCE INFORMATION
# ============================================================

sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Number of words: {len(words)}")


# ============================================================
# Q64 — EMAIL ANALYZER + MEMBERSHIP
# ============================================================

email = input("Enter email: ")

print(f"@ Present: {'@' in email}")

username, domain = email.split("@")

print(f"Username: {username}")
print(f"Domain: {domain}")


# ============================================================
# Q65 — CHARACTER ANALYZER
# ============================================================

character = input("Enter a character: ")

code = ord(character)

previous_character = chr(code - 1)
next_character = chr(code + 1)

print(f"Character: {character}")
print(f"Code: {code}")
print(f"Previous: {previous_character}")
print(f"Next: {next_character}")


# ============================================================
# Q66 — PRODUCT BILL
# ============================================================

product = input("Enter product: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(
    input("Enter discount percentage: ")
)

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


# ============================================================
# Q67 — DATE ANALYZER
# ============================================================

date = input("Enter date: ")

day, month, year = date.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")

print(date[-4:])


# ============================================================
# Q68 — STRING TRANSFORMATION CHALLENGE
# ============================================================

text = input("Enter text: ")

words = text.split()

first_word = words[0]
second_word = words[1]

print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")
print(f"First Word Reversed: {first_word[::-1]}")
print(f"Second Word Reversed: {second_word[::-1]}")


# ============================================================
# Q69 — STUDENT CODE FORMATTER
# ============================================================

student_code = input("Enter student code: ")

parts = student_code.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]

code = f"{degree}/{branch}/{roll}"

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {code}")


# ============================================================
# Q70 — FINAL STRING + INPUT/OUTPUT CHALLENGE
# ============================================================

full_name = input("Enter full name: ")

words = full_name.split()

first_name = words[0]
last_name = words[-1]

first_upper_part = first_name[:3].upper()
last_lower_part = last_name[-3:].lower()
reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper_part}")
print(f"Last Name (Lower Part): {last_lower_part}")
print(f"Full Name Reversed: {reversed_name}")

