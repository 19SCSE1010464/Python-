# Factorial
f = 1
a = int(input("Enter the no : "))
if a<0:
    print("Factorial cannot find")
elif a==0:
    print("Factorial is 1 ")
else:
    for i in range(1,a+1):
        f=f*i
    print("Factorial is : ",f)

# Fibonnaci
first = 0
second = 1
print(first)
print(second)
for i in range(2,10):
    next = first + second
    first = second
    second = next
    print(next)

#Swapping
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = a
a = b
b = c
print("Enter the value of a :",a)
print("Enter the value of b :",b)

#Reversal of string
string = "Good morning"
a = string.split()
a = a[-1: :-1]
final_str = " ".join(a)
print(final_str)

# Prime no
number = 19
for i in range(2,number):
    if number%i == 0:
        print("It is not prime number")
else:
    print("It is prime no ")

# Armstrong
number = int(input("Enter the no : "))
sum = 0
order = len(str(number))
a = number
while number > 0:
    digit = number%10
    sum = sum+digit**order
    number = number//10
if sum == a:
    print("It is Armstrong no")
else:
    print("It is not armstrong no ")

# Second largest no in a list
list =[67,34,6,7,45,2]
list.sort()
print(list[-2])

#Palindrome no
number = int(input("Enter a number :"))
reverse = 0
a = number
while number>0:
    digit = number%10
    reverse = reverse*10+digit
    number = number//10
if a == reverse:
    print("Palindrome no ")
else:
    print("not palindrome no ")

# Pascal Triangle
no_of_rows = 5
for i in range(no_of_rows):
    print(" "*(no_of_rows-i),end=" ")
    print(" ".join(map(str,str(11**i))))