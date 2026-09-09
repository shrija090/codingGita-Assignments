price = 2000
discount_rate = 15
gst_rate = 18

discount_amount = price * discount_rate / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst_rate / 100
final_price = price_after_discount + gst_amount

print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)