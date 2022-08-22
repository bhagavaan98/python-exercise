"""1) writa a python program to save the object in a file by using pickling"""
##import pickle
##class Employee:
##    def __init__(self,Eno,Ename,Esalary,Elocation):
##        self.Eno=Eno
##        self.Ename=Ename
##        self.Esalary=Esalary
##        self.Elocation=Elocation
##    def display(self):
##        print("The employee number is={}".format(self.Eno))
##        print("The employee name is={}".format(self.Ename))
##        print("The employee salary is={}".format(self.Esalary))
##        print("The employee location is={}".format(self.Elocation))
##e=Employee(100,"bhagavaan",15000,"hyderabad")
##with open("employee.data","wb") as f:
##    pickle.dump(e,f)
##    print("pickling of employee object is completed")
##output:
##pickling of employee object is completed
##€•b       Œ__main__”ŒEmployee”“”)”}”(ŒEno”KdŒEname”Œ
##bhagavaan”ŒEsalary”M˜:Œ	Elocation”Œ	hyderabad”ub.

"""2) writa a python program to read the object from the file by using unpickling"""
##import pickle
##with open("employee.data","rb") as f:
##    obj=pickle.load(f)
##    print("unpickling of employee object is completed")
##    print("printing employee information")
##    obj.display()
##output:
##pickling of employee object is completed
##unpickling of employee object is completed
##printing employee information
##The employee number is=100
##The employee name is=bhagavaan
##The employee salary is=15000
##The employee location is=hyderabad
  
"""3) write a python program to save the dict object in a file by using pickling."""
##import pickle
##d={"name":"bhagavaan","no":25}
##with open("dict.data","wb") as f:
##    pickle.dump(d,f)
##    print("completed")
##output:
##completed

"""4) write a python program to read the dict object from the file by using pickling"""
##import pickle
##with open("dict.data","rb") as f:
##    b=pickle.load(f)
##    print(b)
##output:
##{'name': 'bhagavaan', 'no': 25}

"""5)"""














