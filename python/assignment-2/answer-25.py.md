number = 5829

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)
print("Thousands Digit:", thousands_digit)