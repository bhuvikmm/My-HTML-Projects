x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))

x += y
print("After x+=y, x=", x)

x -= y
print("After x-=y, x=", x)

x *= y
print("After x*=y, x=", x)

x /= y
print("After x/=y, x=", x)

x %= y
print("After x%=y, x=", x)

x **= y
print("After x**=y, x=", x)

x //= y
print("After x//=y, x=", x)