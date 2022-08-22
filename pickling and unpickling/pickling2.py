"""write a python program to save the multiple objects to the file by using pickling"""
"""This file acts as module name module name is=pickling-2"""
"""This is file-1"""
import pickle
class Employee:
    def __init__(self,Eno,Ename,Esalary,Elocation):
        self.Eno=Eno
        self.Ename=Ename
        self.Esalary=Esalary
        self.Elocation=Elocation
    def display(self):
        print("The employee number is={}".format(self.Eno))
        print("The employee name is={}".format(self.Ename))
        print("The employee salary is={}".format(self.Esalary))
        print("The employee location is={}".format(self.Elocation))
