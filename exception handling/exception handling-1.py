"""1)Try except"""
##a=10
##b=0
##d=a/b
##print(d)

##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##    print("Inside try")
##except ZeroDivisionError:
##    print("Division by zero not allowed")
##print("rest of the code")
##output:
##Division by zero not allowed
##rest of the code




"""2)Try except else"""
##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##    print("inside try")
##except ZeroDivisionError:
##    print("Division by zero not allowed")
##else:
##    print("inside else")
##print("rest of the code")
##output:
##Division by zero not allowed
##rest of the code


"""3)try except else finally"""
##a=10
##b=9
##try:
##    d=a/b
##    print(d)
##    print("inside try")
##except ZeroDivisionError:
##    print("Division by zero not allowed")
##else:
##    print("inside else")
##finally:
##    print("inside finally")
##print("rest of the code")
##output:
##1.1111111111111112
##inside try
##inside else
##inside finally
##rest of the code

"""4)Except obj"""
##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##    print("inside try")
##except ZeroDivisionError as obj:
##    print(obj)
##print("rest of the code")
##output:
##division by zero
##rest of the code


"""5)except multiple"""
##a=10
##b=9
##try:
##    d=a/0
##    print(d)
##except ZeroDivisionError as obj:
##    print(obj)
##except NameError as ob:
##    print(ob)
##print("rest of the code")
##output:
##division by zero
##rest of the code

"""6)except multiple"""
##a=10
##b=0
##try:
##    d=a/g
##    print(d)
##except (NameError, ZeroDivisionError) as obj:
##    print(obj)
##print("rest of the code")
##output:
##name 'g' is not defined
##rest of the code

"""7)"""
##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##except:
##    print("Exception Handler")
##print("rest of the code")
##output:
##Exception Handler
##rest of the code

"""8)Assert statement"""
##a=20
##assert a<=10
##output:
##AssertionError
##

"""9)custome exception"""
##class BalanceException(Exception):
##    def __init__(self,arg):
##        self.msg=arg
##def checkbalance():
##    money=10000
##    withdraw=9000
##    try:
##        balance=money-withdraw
##        if(balance<=2000):
##            raise BalanceException("insufficient balance")
##        print(balance)
##    except BalanceException as be:
##        print(be)
##checkbalance()
##output:
##insufficient balance



    
    








