binary_num = input("Enter the binary digit : ")

decimal_num = 0

temp = 1
for i in reversed(binary_num):
    decimal_num += int(i)*temp 
    temp *= 2

print(f"The decimal value of binary number {binary_num} is : ", decimal_num)