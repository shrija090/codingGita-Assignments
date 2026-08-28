## C. Code Understanding

### Q-21.
Identify the comment in the following code:
```python
# Display a message
print("Hello")
```
### Ans(21):
The comment is: # Display a message

It explains what the following line of code does. Comments are ignored by Python when the program runs.


### Q-22.
What is the purpose of the following comment?
```python
# Store the student's name
student_name = "Rahul"
```
### Ans(22):
The comment: # Store the student's name

explains that the variable student_name is being used to store the student's name.


### Q-23.
Which of the following names is easier to understand for storing a student's name?
```text
x
student_name
a
```
Explain your answer.
### Ans(23):
student_name is easier to understand.

Explanation:
student_name clearly describes what information the variable stores. Names such as x and a do not provide meaningful information about the value.


### Q-24.
Identify which names are written in `snake_case`:
```text
student_name
StudentName
total_marks
TOTAL_MARKS
```
### Ans(24):
The names written in snake_case are:
(i)student_name
(ii)total_marks

Explanation:
In snake_case, words are written in lowercase and separated using underscores (_).

Examples:
student_name
total_marks


### Q-25.
Which of the following is a commonly used class naming style?
```text
student_record
StudentRecord
STUDENT_RECORD
```
### Ans(25):
StudentRecord is a commonly used class naming style in Python.

Explanation:
Python classes commonly use PascalCase, also called CapWords, where each word starts with a capital letter.

Example:
class StudentRecord:pass


### Q-26.
Consider:
```python
name = "Rahul"
Name = "Amit"
```
Are `name` and `Name` treated as the same name in Python? Explain why.
### Ans(26):
No. name and Name are treated as different names in Python.

Explanation: Python is case-sensitive. This means uppercase and lowercase letters are different.

For example:name = "Rahul"
            Name = "Amit"
            print(name)
            print(Name)

Output:Rahul
       Amit
Therefore, name, Name, and NAME can all represent different variables.


### Q-27.
What is wrong with using names such as `x`, `y`, and `z` everywhere in a large program? Is using short names always wrong?
### Ans(27):
Using names such as x, y, and z everywhere can make a large program difficult to understand and maintain.

For example:
x = 85
It is not immediately clear what x represents.

A more meaningful name would be:
student_marks = 85
Now it is clear that the value represents a student's marks.
However, short names are not always wrong. They can be useful when their meaning is obvious and their scope is small.



___________________________________________________________________________________________________________________________

## D. Practical Problems

### 28.
Create a Python file named:
```text
welcome.py
```
Write a small program that displays a welcome message. Add one useful comment describing the purpose of the program.
### Ans(28):


### 29.
Create a Python file named:
```text
student.py
```
Write a small program containing a student's name and age. Use meaningful names and add a useful comment.
### Ans(29):


### 30.
Create a Python file named:
```text
about_python.py
```
Write a small Python program that contains a comment explaining what Python is and displays a short message about learning Python.
### Ans(30):
