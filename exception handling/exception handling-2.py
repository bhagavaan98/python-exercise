"""syntax error"""
##x=10
##if x==10
##    print("The x value is 10")

##print "hello everyone"

"""run time error"""
##a=int(input("Enter any number="))
##b=int(input("Enter any number="))
##print("The value is=",a/b)
####output:
####Enter any number=10
####Enter any number=2
####The value is= 5.0
####Enter any number=10
####Enter any number=0
####ZeroDivisionError: division by zero
##
##Enter any number=ten
##ValueError: invalid literal for int() with base 10: 'ten'

"""4)run time error"""
##f=open("xyzxyz.txt")
##print(f.read())
##output:
##FileNotFoundError: [Errno 2] No such file or directory: 'xyzxyz.txt'

"""5) how to print exception information"""
##try:
##    print(10/0)
##except ZeroDivisionError as msg:
##    print("The type of the exception is=",type(msg))
##    print("another way is to print the exception")
##    print("The type of the exception is=",msg.__class__)
##    print("The exception class name is=",msg.__class__.__name__)
##    print("The description of the exception is =",msg)
####output:
##The type of the exception is= <class 'ZeroDivisionError'>
##another way is to print the exception
##The type of the exception is= <class 'ZeroDivisionError'>
##The exception class name is= ZeroDivisionError
##The description of the exception is = division by zero

"""3)how to print exception information"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except BaseException as msg:
##    print("The type of exception of the exception is=",type(msg))
##    print("The type of exception of the exception is=",msg.__class__)
##    print("The type of exception of the exception is=",msg.__class__.__name__)
##    print("The type of exception of the exception is=",msg)
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##Enter any number=10
##Enter any number=0
##The type of exception of the exception is= <class 'ZeroDivisionError'>
##The type of exception of the exception is= <class 'ZeroDivisionError'>
##The type of exception of the exception is= ZeroDivisionError
##The type of exception of the exception is= division by zero
##Enter any number=10
##Enter any number=two
##The type of exception of the exception is= <class 'ValueError'>
##The type of exception of the exception is= <class 'ValueError'>
##The type of exception of the exception is= ValueError
##The type of exception of the exception is= invalid literal for int() with base 10: 'two'

"""4) try with multiple except blocks"""
"""syntax"""
##try:
##    -------
##    -------
##    -------
##except ZeroDivisionError:
##    perform alternative arthmatic operations
##except FileNotFoundError:
##    use local file insted of remote file

"""5) try with multiple except blocks"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except ZeroDivisionError:
##    print("cannot divide with zero")
##except ValueError:
##    print("please provide int value only")
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##---------------------
##Enter any number=10
##Enter any number=0
##cannot divide with zero
##------------------------
##Enter any number=10
##Enter any number=two
##please provide int value only

"""6)try with multiple except blocks"""
##try:
##    print(10/0)
##except ZeroDivisionError:
##    print("cannot divide with zero")
##except ArithmeticError:
##    print("Arithmetic error")
##output:
##cannot divide with zero

"""7) try with multiple except blocks"""
##try:
##    print(10/0)
##except ArithmeticError:
##    print("Arithmetic error")
##except ZeroDivisionError:
##    print("cannot divide with zero")
##output:
##Arithmetic error

"""8) single except block that can handle multiple different exceptions."""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except (ZeroDivisionError,ValueError) as msg:
##    print("The raised exception is=",msg.__class__.__name__)
##    print("description of the exception is=",msg)
##    print("please provide valid input only")
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##----------------------
##Enter any number=10
##Enter any number=0
##The raised exception is= ZeroDivisionError
##description of the exception is= division by zero
##please provide valid input only
##----------------------
##Enter any number=10
##Enter any number=two
##The raised exception is= ValueError
##description of the exception is= invalid literal for int() with base 10: 'two'
##please provide valid input only

"""default except block"""
"""syntax"""
##except:
##    statements

"""9) wap by using default except block"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except ZeroDivisionError:
##    print("can not divide with zero")
##except:
##    print("provide integer value only")
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##------------------------
##Enter any number=10
##Enter any number=0
##can not divide with zero
##-------------------------
##Enter any number=10
##Enter any number=two
##provide integer value only

"""10) wap by using only default except block"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except:
##    print("provide valid input only")
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##--------------------
##Enter any number=10
##Enter any number=0
##provide valid input only
##------------------------
##Enter any number=10
##Enter any number=two
##provide valid input only

"""11)wap by using default except block"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except:
##    print("provide integer value only")
##except ZeroDivisionError:
##    print("can not divide with zero")
##output:
##default except block must be last.

"""12)wap by using default except block"""
##try:
##    x=int(input("Enter any number="))
##    y=int(input("Enter any number="))
##    print("The result is=",x/y)
##except ZeroDivisionError:
##    print("can not divide with zero")
##except ValueError:
##    print("provide integer value")
##except:
##    print("provide valid value only")
##output:
##Enter any number=10
##Enter any number=2
##The result is= 5.0
##
##Enter any number=10
##Enter any number=0
##can not divide with zero
##
##Enter any number=10
##Enter any number=two
##provide integer value

"""13) Various possible combinations of except blocks: """
##1) except ZeroDivisionError:
##2) except (ZeroDivisionError):
##3) except ZeroDivisionError as msg: 
##4) except (ZeroDivisionError) as msg: 
##5) except (ZeroDivisionError,ValueError):
##6) except (ZeroDivisionError,ValueError) as msg: 
##7) except:
##invalid combinations:
##1) (except ZeroDivisionError as msg):
##2) except ZeroDivisionError,ValueError:
##3) except (ZeroDivisionError,ValueError as msg): 

"""finally block purpose and specialty"""
##try:
##    print("risky code")
##except:
##    print("handling code")
##finally:
##    print("clean up code")
##"""try to maintain risky code, except to maintain handling code and finally block to maintain clean up code."""

"""14) wap to handle the exception if there is no exception."""
##try:
##    print("try")
##except:
##    print("except")
##finally:
##    print("finally")
##output:
##try
##finally

"""15) if exception raised and handled"""
##try:
##    print("try")
##    print(10/0)
##except ZeroDivisionError:
##    print("except")
##finally:
##    print("finally")
##output:
##try
##except
##finally

"""16) if exception raised but not handled"""

























