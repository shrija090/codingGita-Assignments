number = 5834

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Thousands Place:", thousands_digit * 1000)
print("Hundreds Place:", hundreds_digit * 100)
print("Tens Place:", tens_digit * 10)
print("Ones Place:", ones_digit)