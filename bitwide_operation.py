#Task 1 : Calculate the highest possible number with 4 bits?

decimal = 2 ** 4 - 1
binary = bin(decimal)
print(binary)

"""Task 2 : Check if the following numbers are even or odd with the bitwise and operator.
Print out the given numbers (num1 to num6) in decimal and binary format.
print 0 if the number is even and 1 if the number is odd"""

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
num6 = 6


print(num1, bin(num1), num1 % 2)
print(num2, bin(num2), num2 % 2)
print(num3, bin(num3), num3 % 2)
print(num4, bin(num4), num4 % 2)
print(num5, bin(num5), num5 % 2)
print(num6, bin(num6), num6 % 2)

"""Task 3 : Assign to the variable c the result of the XOR operation of a and b.
Then use the XOR operation of c and ___ to get back the value of a. Assign the result to d."""

a = 3
b = 5

c = a ^ b

print( bin(a), '^', bin(b), '=', bin(c), )

d = c ^ b

print( bin(c), '^', bin(b), '=', bin(d),)


#Task 4 : Swap the values of a and b by using the XOR operator.

a = 2

b = 5

c = a ^ b

t = c ^ a

z = c ^ b

print('before swap : a = ',a , 'b =', b, "after swap: a =", t, "b =", z, )


#Task 5 : Left shift a number by certain number of bits.

a = 4

amount1 = 5

amount2 = 90

amount3 = 28

amount4 = 2

d = a << amount1
t = a << amount2
o = a << amount3
m = a << amount4

print(d, t, o, m,)
print(bin(d), bin(t), bin(o), bin(m),)


#Task 6 : Right shift the number 28 by 2 bits.

a = 28
b = 2

c = a >> b

print(c)