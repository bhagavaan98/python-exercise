"""This is file-2"""
"""receiver is resposible to unpickled employee object"""
import pickle
f=open("employee.dat","rb")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("all employees completed")
        break

    
output-1:
The employee number is=22108
The employee name is=bhagavaan
The employee salary is=15000
The employee location is=hyderabad
The employee number is=22110
The employee name is=ramesh
The employee salary is=16500
The employee location is=chennai
Traceback (most recent call last):
  File "E:/bhagavaan/oop's/pickling and unpickling/pickling-4.py", line 5, in <module>
    obj=pickle.load(f)
EOFError: Ran out of input

output-2:
The employee number is=22108
The employee name is=bhagavaan
The employee salary is=15000
The employee location is=hyderabad
The employee number is=22110
The employee name is=ramesh
The employee salary is=16500
The employee location is=chennai
all employees completed
