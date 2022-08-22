"""1)"""
##class Student:
##    def __init__(self,id,name):
##        self.id=id
##        self.name=name
##    def display(self):
##        print("my id is ={}".format(self.id))
##        print("my name is={}".format(self.name))
##s=Student(22108,"bhagavaan")
##s.display()
##s.__setattr__("grade","A")
##print(getattr(s,"grade"))
##      
####output:
##my id is =22108
##my name is=bhagavaan
##A

"""2)"""
##class Student:
##    def __init__(self,id,name):
##        self.id=id
##        self.name=name
##    def display(self):
##        print("my id is={}".format(self.id))
##        print("my name is={}".format(self.name))
##s=Student(22108,"bhagavaan")
##s.display()
##s.__setattr__("grade","A")
##print(getattr(s,"grade"))



"""setattr() is used to assign a new value to an object/instance attribute.
syntax:
setattr(object,name,value)"""
"""3)"""
##class Details:
##    name="bhagavaan"
##    age=25
##d=Details()
##print("name before modification={}".format(d.name))
##print("age before  modification={}".format(d.age))
##setattr(d,"name","rakesh")
##setattr(d,"age",27)
##print("name after modification={}".format(d.name))
##print("age after modification={}".format(d.age))
##
##output:
##name before modification=bhagavaan
##age before  modification=25
##name after modification=rakesh
##age after modification=27

"""4)"""
##class student:
##    def setvalues(self,name,age,grade):
##        self.name=name
##        self.age=age
##        self.grade=grade
##    def getvalues(self):
##        print("my name is={}".format(self.name))
##        print("my age is={}".format(self.age))
##        print("my grade is={}".format(self.grade))
##s=student()
##s.setvalues("bhagavaan",25,"A")
##s.getvalues()

##output:
##my name is=bhagavaan
##my age is=25
##my grade is=A














