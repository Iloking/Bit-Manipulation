a = 5
print("Bin af a:", bin(a))
b = ~a
print("Not:", b)
print("Bin of b:", bin(b))

a = 10
b = 6
print(bin(a))
print(bin(b))
print(a & b)
print(bin(a&b))

a =8
b = 5
print(bin(a))
print(bin(b))
print(bin a │ b)
print(bin(a │ b))

a = 10
b = 8
print(bin(a))
print(bin(b))
print(a ^ b)
print(bin(a ^ b))

a = 10
print(a << 1)  # Left shift by 1 multiplies the number by 2

a = 10
print(a >> 1)  # Right shift by 1 divides the number by 2
num = 23

if num ^ 1 == (num + 1):
    print(num, "is even")
else:
    print(num, "is odd")

num = 20
print(bin(num))

counter = 0

while num > 0:
    counter = counter + 1
    num = num >> 1

print(counter)

