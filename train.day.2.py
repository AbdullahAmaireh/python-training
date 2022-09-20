

"""is_hot = True

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
print("enjoy your day")"""

"""
is_hot = False

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")
print("enjoy your day")"""

"""is_hot = False

if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")

else:
    print("its a cold day")
    print("wear warm clothes")
print("enjoy your day")"""

"""is_hot = False
is_cold = False
if is_hot:
    print("it's a hot day")
    print("Drink plenty of water")

elif is_cold :
    print("its a cold day")
    print("wear warm clothes")

else:
   print("its a lovely day")
print("enjoy your day")"""

"""
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment =(0.1 * price)

else:
    down_payment = (0.2 * price)
print(f"down payment: ${down_payment}")"""


#dont forget to use (f)and{}

"""has_high_income =True
has_good_credit = True
if has_high_income and has_good_credit:
    print("eligible for loan")"""

"""has_high_income =False
has_good_credit = True
if has_high_income and has_good_credit:
    print("eligible for loan")"""

"""has_high_income =False
has_good_credit = True
if has_high_income or has_good_credit:
    print("eligible for loan")"""

"""has_high_income =False
has_good_credit = True
if has_good_credit and not has_high_income:
    print("eligible for loan")"""

"""has_high_income =True
has_good_credit = True
if has_good_credit and not has_high_income:
    print("eligible for loan")"""


    #AND both condition should be true
    #OR both condition should be true
    #NOT will convert the False to true

"""tempereture = 30
if tempereture > 30:
    print("its hot")
else:
    print("its cold")"""

"""name = "abdullah"
if len (name) <3:
    print("name must be at least 3 characters ")
elif len(name) >50:
    print("name must be a maximum 50 characters")
else:
    print("your name is look good")

weight =  int(input("weight: "))
unit = input('(L)bs or (k)g' )

if unit.upper() == "L":
    converted =weight * 0.45
    print(f"you are {converted} kilos")

else:
    converted = weight / 0.45
    print(f"you are {converted} pounds") """

"""i = 1
while i <= 5:
    print(i)
    i= i + 1
print("done")"""

"""i = 1
while i <= 5:
    print('*' * i)
    i= i + 1
print("done")
"""


"""secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess:  '))
    guess_count +=1
    if guess ==secret_number:
        print("you won")
        break
else:
    print("sorry you field")"""    

"""command = ""
while True:
    command = input("> ").lower()
    if command  == "start":
        print("car started....")
    elif command == "stop":
        print("car stopped...")
    elif command == "help":
        print("
            start - to start the car
            stop - to stop the car
            quit - to quit
            ")
    elif command =="quit":
        break
    else:
        print("sorry i dont inderstand that")"""


"""for item in 'python':
    print(item)"""


"""for item in ['abdullah', 'John', 'sarah']:
    print(item)
"""
"""for item in range(10):
    print(item)
"""


"""for item in range(5, 10 ):
    print(item)"""


"""for item in range(5, 10 , 2):
    print(item)
"""

"""prices = [10 , 20 , 30]

total = 0
for price in prices:
    total += price
print(f"total:{total}")
"""


"""for x in range(4):
    print(x)"""

"""for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
"""


"""number = [5,2,5,2,2]
for x_count in number:
    print('x' * x_count)"""

"""number = [1,1,1,1,5]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)"""

"""names = ['John', 'bob' , 'Sarah' , 'abdullah' , 'Mary']
print(names)"""

names = ['John', 'bob' , 'Sarah' , 'abdullah' , 'Mary']
print(names[2:4])

    



