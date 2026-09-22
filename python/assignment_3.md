# Assignment 3 — Operators, Strings, Input & Output

## Q1
```python
a = 15
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
```

Output:
```text
True
False
False
True
True
False
```

## Q2
```python
x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
```

Output:
```text
True
False
False
True
True
```

## Q3
```python
a = 10
b = 5

print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)
```

Output:
```text
True
True
False
True
```

## Q4
```python
print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")
```

Output:
```text
True
False
True
```

## Q5
```python
x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x)
```

Output:
```text
10
```

Values:
```text
20 → 30 → 25 → 50 → 10
```

## Q6
```python
marks = 50

marks += 10
marks -= 5
marks *= 2

print(marks)
```

Output:
```text
110
```

## Q7
```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)
```

Output:
```text
True
False
False
```

## Q8
```python
word = "computer"

print("p" in word)
print("x" in word)
print("c" not in word)
```

## Q9
```python
text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)
```

Output:
```text
True
False
True
False
```

## Q10
```python
text = input("Enter a word or sentence: ")

print("a" in text)
```

## Q11
```python
email = input("Enter email: ")

print("@" in email)
```

## Q12
```python
print(ord("A"))
print(ord("a"))
print(ord("Z"))
print(ord("z"))
print(ord("0"))
print(ord("9"))
print(ord("@"))
```

Output:
```text
65
97
90
122
48
57
64
```

## Q13
```python
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(48))
print(chr(57))
print(chr(64))
```

Output:
```text
A
B
a
b
0
9
@
```

## Q14
```text
ord("A") = 65
ord("a") = 97
ord("B") = 66
ord("b") = 98

1. ord("a") is larger.
2. Difference = 32
3. Yes, difference = 32
```

## Q15
```python
character = input("Enter a character: ")

print(ord(character))
```

## Q16
```python
character = input("Enter a character: ")

print(chr(ord(character) + 1))
```

## Q17
```python
print("A" < "B")
print("a" < "b")
print("A" < "a")
print("0" < "9")
```

Output:
```text
True
True
True
True
```

## Q18
```python
print(chr(9731))
print(chr(9829))
print(chr(8377))

print(ord("☃"))
print(ord("♥"))
print(ord("₹"))
```

Output:
```text
☃
♥
₹
9731
9829
8377
```

## Q19
```python
text = "PYTHON"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])
```

Output:
```text
P
Y
N
O
```

## Q20
```python
text = "COMPUTER"

print(text[0])
print(text[3])
print(text[-1])
print(text[-3])
```

Output:
```text
C
P
R
E
```

## Q21
```python
text = "PYTHON"

print(text[0])
print(text[2])
print(text[-1])
print(text[-2])
```

Output:
```text
P
T
N
O
```

## Q22
```python
word = input("Enter a word: ")

print(word[0])
print(word[-1])
```

## Q23
```python
word = "PROGRAM"

print(word[0])
print(word[2])
print(word[-1])
print(word[-4])
```

Output:
```text
P
O
M
G
```

## Q24
```python
text = "PYTHON"

print(text[0:3])
print(text[2:5])
print(text[1:6])
```

Output:
```text
PYT
THO
YTHON
```

## Q25
```python
text = "PROGRAMMING"

print(text[:4])
print(text[4:])
print(text[:])
```

Output:
```text
PROG
RAMMING
PROGRAMMING
```

## Q26
```python
text = "COMPUTER"

print(text[-5:])
print(text[:-3])
print(text[-6:-2])
```

Output:
```text
PUTER
COMPU
OMPU
```

## Q27
```python
text = "PYTHON"

print(text[::2])
print(text[1::2])
print(text[::-1])
```

Output:
```text
PTO
YHN
NOHTYP
```

## Q28
```python
text = input("Enter a string: ")

print(text[::-1])
```

## Q29
```python
text = input("Enter a string: ")

print(text[::2])
```

## Q30
```python
text = input("Enter a string: ")

print(text[:3])
print(text[-3:])
```

## Q31
```python
text = "ABCDEFGHIJ"

print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])
```

Output:
```text
CEG
IGE
JHFDB
```

## Q32
```python
text = "BTECH-CSE-2026"

print(text[:5])
print(text[6:9])
print(text[10:])
```

Output:
```text
BTECH
CSE
2026
```

## Q33
```python
text = "Python is easy"

print(text.split())
```

Output:
```text
['Python', 'is', 'easy']
```

## Q34
```python
data = "apple,banana,mango"

print(data.split(","))
```

Output:
```text
['apple', 'banana', 'mango']
```

## Q35
```python
text = "Python is easy"

print(text.split(","))
```

Output:
```text
['Python is easy']
```

## Q36
```python
text = input("Enter full name: ")

words = text.split()

print(words[0])
print(words[1])
print(words[2])
```

## Q37
```python
first_name, last_name = input("Enter first and last name: ").split()

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
```

## Q38
```python
a, b, c = input("Enter three numbers: ").split()

a = int(a)
b = int(b)
c = int(c)

print(a + b + c)
```

## Q39
```python
data = input("Enter student record: ")

name, age, course, city = data.split(",")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"City: {city}")
```

## Q40
```python
email = input("Enter email: ")

username, domain = email.split("@")

print(f"Username: {username}")
print(f"Domain: {domain}")
```

## Q41
```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Total words: {len(words)}")
```

## Q42
```python
print("Hello\nWorld")
```

## Q43
```python
print("Name:\tRahul")
print("Age:\t20")
print("City:\tAhmedabad")
```

## Q44
```python
print("C:\\Python\\Programs")
```

## Q45
```python
print("It\'s Python")
```

## Q46
```python
print("He said \"Hello\"")
```

## Q47
```python
print("Python\nProgramming")
```

Output:
```text
Python
Programming
```

## Q48
```python
print("Student Details\n")
print("Name:\tRahul")
print("Age:\t20")
print("Course:\tB.Tech")
```

## Q49
```python
print("2026", "09", "09", sep="-")
```

Output:
```text
2026-09-09
```

## Q50
```python
print("Hello", end=" ")
print("Python")
```

Output:
```text
Hello Python
```

## Q51
```python
print("10", "20", "30", sep="-")
print("40", "50", "60", sep="-")
```

## Q52
```python
name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
course = input("Enter course: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course: {course}")
```

## Q53
```python
price = float(input("Enter price: "))

print(f"{price:.2f}")
```

## Q54
```python
age = int(input("Enter age: "))

print("Age after 5 years:", age + 5)
```

## Q55
```python
print("It's Python")
```

## Q56
```python
text = "Python"

print(text[1:4])
```

## Q57
```python
a, b = input().split()

print(a)
print(b)
```

## Q58
```python
a, b = input().split()

print(a + b)
```

Output:
```text
1020
```

Correct numeric addition:
```python
a, b = input().split()

a = int(a)
b = int(b)

print(a + b)
```

Output:
```text
30
```

## Q59
```python
print("C:\\new\\test")
```

## Q60
```python
name = input("Enter name: ")
marks = input("Enter three marks: ").split()

mark1 = int(marks[0])
mark2 = int(marks[1])
mark3 = int(marks[2])

total = mark1 + mark2 + mark3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
```

## Q61
```python
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
```

## Q62
```python
name = input("Enter full name: ")

parts = name.split()

first_name = parts[0]
last_name = parts[-1]

username = first_name.lower() + "." + last_name.lower()

print(username)
```

## Q63
```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Number of words: {len(words)}")
```

## Q64
```python
email = input("Enter email: ")

print(f"@ Present: {'@' in email}")

username, domain = email.split("@")

print(f"Username: {username}")
print(f"Domain: {domain}")
```

## Q65
```python
character = input("Enter a character: ")

code = ord(character)
previous = chr(code - 1)
next_character = chr(code + 1)

print(f"Character: {character}")
print(f"Code: {code}")
print(f"Previous: {previous}")
print(f"Next: {next_character}")
```

## Q66
```python
product = input("Enter product: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount: "))

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")
```

## Q67
```python
date = input("Enter date: ")

day, month, year = date.split("-")

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")

print(date[-4:])
```

## Q68
```python
text = input("Enter text: ")

words = text.split()

first_word = words[0]
second_word = words[1]

print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")
print(f"First Word Reversed: {first_word[::-1]}")
print(f"Second Word Reversed: {second_word[::-1]}")
```

## Q69
```python
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
```

## Q70
```python
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
```
