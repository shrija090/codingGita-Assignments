number = 4726

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = (number // 100) % 10
thousands_digit = number // 1000

reversed_number = ones_digit * 1000 + tens_digit * 100 + hundreds_digit * 10 + thousands_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)