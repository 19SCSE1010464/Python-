# Remove Duplicates
numbers = [2,2,4,6,7,6,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Greatest Number
numbers = [6,7,10,8,2,1]
max = numbers[0]
for number in numbers:
    if number>max:
        max = number
print(max)

# 1234 to one two three four
phone = input("Phone: ")
dict_digits = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five'
}
output = ""
for ch in phone:
    output+=dict_digits.get(ch,"!")+" "
print(output)
# Fizz Buzz
def fizz_buzz(input):
    if input%3 == 0 and input%5 == 0:
        return 'fizz_buzz'
    if input%3 == 0:
        return 'fizz'
    if input%5 == 0:
        return 'buzz'
    return input
print(fizz_buzz(3))

# function
def sal_fun(first_name,last_name): # first_name and last_name (parameters)
    print(f"hello my name is :{first_name},{last_name}")
    print("nice to meet u")


print('Good morning')
sal_fun('saloni','kumari') #saloni and kumari(arguments)
print("bye")
# Exception
try:
    age = int(input('Age:'))
    print(age)
    income = 2000
    risk = income/age
except ZeroDivisionError:
    print('Age cannot bw 0')
except ValueError:
    print('Invalid value')

# Constructor
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'I am {self.name}')

sal = Person("saloni")
sal.talk()

# Importing Random values
import random
class Sal:
    def number(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
salobj = Sal()
print(salobj.number())

# files and directories
from pathlib import Path
path = Path('ecommerce')
print(path.exists())
# or path.mkdir (make directory) ,path.rmdir(remove dir...)
# or for file in path.glob('*.py'): py files in directory or *










