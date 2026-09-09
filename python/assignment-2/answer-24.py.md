number = 746

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

print("Ones Digit:", ones_digit)
print("Tens Digit:", tens_digit)
print("Hundreds Digit:", hundreds_digit)