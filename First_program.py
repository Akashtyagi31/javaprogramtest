#List
values = [1, 2, 3, 4, "Akash"]
values.insert(4,5)
print(values)
values.remove(5)
print(values)

#f-string
fname = "Akash"
lname = "Tyagi"
print(f'{fname} {lname}')

#List
a = [10,20,30,40,[50,55,[65,75]]]
print(a[4][2][1])

#For loops
names = ["Akash", "Krishna", "Rohan", "Hitesh", "Naman"]
for new in names:
    print(f'Hello {new}!')
    if new == "Rohan":
        print(f'My name is {"Rohan"}')
    else:
        print("Other names")

#While loops
new = ''
while new != '0':
    new = input("Enter a random number: ")
    print(f'new number is- {new}')
print("You guessed it right!")

#Function
def Name():
    name = input("Enter Name: ")
    print(f'Hello {name}')

Name()

######################################
def Number(exact_number):
    new = ''
    while new != exact_number:
        new = int(input("Enter a random number from 0 to 100: "))
        if new > 50:
            print(f'{new} -number is greater than 50')
        else:
            print(f'{new} -number is less than 50')
    print("You guessed it right!")

Number(99)

#return function
def sum(a,b):
    return a+b
c=sum(3,4)
print(c)
