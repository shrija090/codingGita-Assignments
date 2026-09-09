number = 9365

thousands_digit = number // 1000
hundreds_digit = (number // 100) % 10
tens_digit = (number // 10) % 10
ones_digit = number % 10

print("Thousands Digit:", thousands_digit)
print("Hundreds Digit:", hundreds_digit)
print("Tens Digit:", tens_digit)
print("Ones Digit:", ones_digit)