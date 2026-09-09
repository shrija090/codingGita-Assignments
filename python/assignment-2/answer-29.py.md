number = 583

ones_digit = number % 10
tens_digit = (number // 10) % 10
hundreds_digit = number // 100

reversed_number = ones_digit * 100 + tens_digit * 10 + hundreds_digit

print("Original Number:", number)
print("Reversed Number:", reversed_number)