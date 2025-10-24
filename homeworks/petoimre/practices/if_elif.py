# if elif else

x = 11
y = 3

# artimetic operators  +  -  *  /  %  **  //

# maradékosztás
z = x % y
print(z)          # eredmény 1

# hatványozás
z = x ** y
print(z)          # eredmény 1331   11 a harmadikon


# kerekített osztás  //
z = x // y
print(z)          # eredmény 3


# assigment operators   =  +=  -=  *=  /=

x = 5

x += 3           # ua      X = x + 3
x -= 3           # ua      X = x - 3
x *= 3           # ua      X = x * 3
x /= 3           # ua      X = x / 3

# comparison operators    ==  !=  >  <  >=  <=

x = 11
y = 3

z = x == y       #     x egyenlő y-al?    eredmény False 
z = x != y       #     x NEM egyenlő y-al?    eredmény True


# logical operators  and  or  not
# ha zárójelben van, az lesz először kiértékelve. ha nincs, akkor az and az első és balról jobbra a sorrend.
# and-nél, ha az egyik oldal False, az eredmény biztos False

z = x < 10 and x > 5           # True 
z = x < 10 or x > 5            # True
z = not(x < 10 and x > 5)      # False     először a zárójel lesz kiértékelve. utána a not negálja
z = not x < 10 and x > 5       # False     balról jobbra halad. not x < 10 az első kif. és x > 5  a másik kif. köztük az and
z = x < 10 and x == 5          # False
z = x < 10 and x > 5           # True 
a = True and True              # True
b = True and False             # False   Ha az egyik False, az eredmény mindig False
c = False and False            # False   Ha az egyik False, az eredmény mindig False
d = True or True               # True    Ha legalább z egyik True, az eredmény biztos True
e = True or False              # True    Ha legalább z egyik True, az eredmény biztos True
f = False or False             # False   Csak akkor false, ha mindkettő false

# identity operators    is  is not
# a memória címet hasonlítja össze

x = [1,2,3]
y = [1,2,3]
print(id(x))
print(id(y))

print(x is y)        # False
print(x is not y)    # True

# membership operators   in    not in
# benne van-e a listában?
# lisák, dictionary-k...

z = x in [1]              # az 1 benne van-e a listában?    True
z = x not in [1]          # ugye az 1 nincs benne a listában?   False, mert benne van


# operator precedence
# szorzás és az osztás magasbb rendű mint az összeadás és kivonás
# először mindig a zárójelben lévő kerül kiértékelésre
# balról jobbra halad
# az and mindig hamarabb hajódik végre mint az or


a = 2 + 3 * 4                   # a = 14     első a szorzás: 3 * 4 = 12.   utána: 12 + 2 = 14
b = (2 + 3) * 4                 # b = 20     első a zárójel: 2 + 3 = 5.    utána: 5 * 4 = 20
c = 10 - 3 * 2 + 5              # c = 9      első a szorzás: 3 * 2 = 6.  utána: 10 - 6 = 4.  utána: 4 + 5 = 9
d = (10 - 3) * (2 + 5)          # d = 49     első az első zárójel: 10 - 3 = 7, utána a második zárójel: 2 + 5 = 7, utána a szorzás: 7 * 7 = 49
e = 2 ** 3 + 1                  # e = 9      első a hatványra emelés: 2 * 2 = 4, 4 * 2 = 8. utána: 8 + 1 = 9
f = 2 ** (3 + 1)                # f = 16     első a zárójel: 3 + 1 = 4. utána a hatványra emelés: 4 * 4 = 16
g = 10 / 2 * 5                  # g = 25     balról jobbra: 10 / 2 = 5. utána: 5 * 5 = 25
h = 10 / (2 * 5)                # h = 1      először a zárójel: 2 * 5 = 10. utána: 10 / 10 = 1
i = True or False and False     # i = True   először: False and False --> False. utána jön a True or (kapott)False
j = (True or False) and False   # j = False  itt a zárójelet értékeli ki először, ami True. utána jön a (kapott)True and False


# short circuit evaluation
a = True and False and True and True and False
# balról jobbra halad. az első True and False -nél eldőlt, hogy az eredmény nem lehet más csak is False. Ezért itt kiszáll.

y_n = True

if y_n == True:
    print("y_n = True")
else:
    print("y_n = False")

# truth-falsy szerinti kiértékelés    ez a pythonic!
x = 1

if x:                           # truth-falsy szerint = True, mert nem 0
    print("x = True")
else:
    print("x = False")

# if-elif-else
number = 10

if number == 10:
    print("Number is 10")
elif number == 11:
    print("Nunber is 11")
elif number == 12:
    print("Number is 12")
else:
    print("Number is someting else")
# az első ág ami True, kiszáll!

fruits = ["rapsberry", "banana", "cherry", "watermelon"]

if "cherry" in fruits:
    print("cherry is in fruits")
elif "banana" in fruits:
    print("banana is in fruits")   # mindkettő benne van, de a cherry-nél kiszáll


if "cherry" in fruits:
    print("cherry is in fruits")
if "banana" in fruits:
    print("banana is in fruits")   # mindkettő benne van, és így mindkettőt kiértékeli

if "banana" in fruits or "cherry" in fruits:
    print("banana or cherry in fruits")   # bármelyik benne van, kiértékeli

if "banana" in fruits and "cherry" in fruits:
    print("banana and cherry in fruits")   # csak ha mindkettő benne van, akkor étékeli ki 

# if-elif-else with logical operators

a = 1
b = 2

if a is b:
    print("the 2 object are the same")
# nem fog történni semm, mert a két obj nem ugyanaz.

# combining multiple and single operators

c = 3

if a is not b and c == 3 and ("cherry" in fruits or "elderflower" in fruits):  
    print("all are True")

# első a zárójel, ami True. 
# utána balról jobbra: a is not b,ami True
# utána c == 3, ami True
# ezek and-el összekötve ami True and True and True = True

# fizz-buzz

n = 15

if n % 3 == 0 and n % 5 == 0:    # maradék osztás eredmény 0
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")    
else:
    print(n)

# bad example

if n % 3 == 0:                  # 15-nél itt kilép és nem megy a következőre !!!
    print("Fizz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")    
else:
    print(n)

# walrus operator

# without warsus
value = 10
if value > 5:
    print(value)

# with warsus

if (value := 10) > 5:   # helyszínen deklarélva a változó
    print(value)

items = ["apple", "cherry", "banana", "date"]

treshold = 3

if (lenght := len(items)) > treshold:
    print(f"the list has {lenght} items, treshold is {treshold}.")

# ternary operator            kizárólag egyszerű esetben!

# without ternary

value = 10
if value > 5:
    print("value > 5")
else:
    print("5 or less")

# with ternary

result = "value > 5" if value > 5 else "5 or less"


# project withrowal
import os

correct_pin = 1234
account_balance = 500.00

pin = int(input("Please enter PIN:"))

if pin == correct_pin:
    print("PIN accepted")
    print(f"Your current balance: $ {account_balance:.1f}")
    withrowal_amount = float(input("Enter the amount you want to withrow: $"))
    if withrowal_amount > 0:
        if withrowal_amount <= account_balance:
            account_balance -= withrowal_amount
            print(f"withroval succesfull! Your new balance is: $ {account_balance:.1f}")
        else:
            print("Insuffcent funds")
    else:
        print("Invalid amount. Please enter positive number!")
else:
    print("Incorrect PIN. Try again!") 









