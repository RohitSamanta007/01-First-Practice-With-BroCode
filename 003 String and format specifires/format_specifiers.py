# format specifiers = {:flags} format a value based on what flags are inserted


price1 = 3000.14159
price2 = -9870.66
price3 = 2400.52

# .(number)f = round to theat many decimal places (fixed point)
print(f"Price 1 is : {price1:.2f}")
print(f"Price 2 is : {price2:.1f}")
print(f"Price 3 is : {price3:.3f}")

# :(number) = allocate that many spaces
print(f"Price 1 is : {price1:10}")
print(f"Price 2 is : {price2:10}")
# :03 = allocate and zero pad that many spaces
print(f"Price 3 is : {price3:010}") # spaces are padded with front zeros


# :< = left justify
print(f"Price 1 is : {price1:<10}.")
print(f"Price 2 is : {price2:<10}.")
print(f"Price 3 is : {price3:<10}.")

# :> = right justify
print(f"Price 1 is : {price1:>10}.")
print(f"Price 2 is : {price2:>10}.")
print(f"Price 3 is : {price3:>10}.")

# :^ = Center align
print(f"Price 1 is : {price1:^10}.")
print(f"Price 2 is : {price2:^10}.")
print(f"Price 3 is : {price3:^10}.")

# :+ = show the positive or nagetive signs for values
print(f"Price 1 is : {price1:+}.")
print(f"Price 2 is : {price2:+}.")
print(f"Price 3 is : {price3:+}.")

# :, = show the comma for thousend
print(f"Price 1 is : {price1:,}.")
print(f"Price 2 is : {price2:,}.")
print(f"Price 3 is : {price3:,}.")
print()

# we can combine multiple format specifiers 
print(f"Price 1 is : {price1:+,.2f}.")
print(f"Price 2 is : {price2:+,.2f}.")
print(f"Price 3 is : {price3:+,.2f}.")
