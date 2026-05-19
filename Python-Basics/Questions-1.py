# String Reverse

a = "Hello World"

for i in range(len(a)-1, -1, -1):
    print(a[i], end='')

# String Palindrome or not

b = 'racecar'

i = 0
j = len(b)-1
palindrome = True

while(i < j):
    if(b[i] == b[j]):
        i += 1
        j -= 1
    else:
        palindrome = False
        print("\nNot Palindrome")
        break

if(palindrome):
    print("\nPalindrome")


# Factorial of a number

c = int(input('Enter a number: '))

fact = 1

for i in range(1, c + 1):
    fact *= i

print(f'factorial of {c} is {fact}')


# Separating digits of a number

d = 234
rev = 0

while( d > 0):
    digit = d % 10
    print(digit)
    rev = rev * 10 + digit

    d = d // 10

print(f'Reversed number: {rev}')

