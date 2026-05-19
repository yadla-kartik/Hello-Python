a = int(input('Enter your age: '))

if a >= 18:
    print("You are eligible to vote")
else:
    print('You are not eligible to vote')


b = int(input('Enter your marks: '))

if b >= 90: 
    print('Grade A')
elif(b>=70 and b<=89):
    print('Grade B')
elif(b>=60 and b<=69):
    print('Grade C')
else: 
    print('Grade D')