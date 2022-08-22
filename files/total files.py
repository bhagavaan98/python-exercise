"""1) write a python program on text files to write the data on files and
read the data read mode and binay mode"""
##f=open("student.txt",mode="w")
##f.write("hello\n")
##f.write("hi\n")
##f.write("hiii\n")
##f.write("how are you")
##f.close()
##print("writting success")
##
##f=open("student.txt",mode="r")
##data=f.read()
##print(data)
##f.close()
##
##f=open("student.txt",mode="rb")
##data=f.read()
##print(data)
##f.close()
##
##output:
##writting success
##hello
##hi
##hiii
##how are you
##b'hello\r\nhi\r\nhiii\r\nhow are you'
##
##
"""2)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="r")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file closed ={}".format(f.closed))
##f.close()
##print("file closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=r
##file is readable=True
##file is writable=False
##file closed =False
##file closed=True
##
"""4)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="w")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file readable={}".format(f.readable()))
##print("file writable={}".format(f.writable()))
##print("file closed={}".format(f.closed))
##f.close()
##print("file closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=w
##file readable=False
##file writable=True
##file closed=False
##file closed=True
##
"""5)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="a")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file readable={}".format(f.readable()))
##print("file writable={}".format(f.writable()))
##print("file closed={}".format(f.closed))
##f.close()
##print("file closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=a
##file readable=False
##file writable=True
##file closed=False
##file closed=True
##
"""6)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not[Exclusive creation mode]"""
##f=open("student2.txt",mode="x")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed ={}".format(f.closed))
##output:
##file name=student2.txt
##file mode=x
##file is readable=False
##file is writable=True
##file is closed=False
##file is closed =True
##
"""7)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="r+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=r+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
"""8)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="w+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=w+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
"""9)write a python program on text files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("student.txt",mode="a+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=student.txt
##file mode=a+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
"""10)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("python.jpg",mode="rb")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##
"""11)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("python.jpg",mode="wb")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=python.jpg
##file mode=wb
##file is readable=False
##file is writable=True
##file is closed=False
##file is closed=True
##
"""12)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("python.jpg",mode="ab")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=python.jpg
##file mode=ab
##file is readable=False
##file is writable=True
##file is closed=False
##file is closed=True
##
"""13)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("pythonExc.jpg",mode="xb")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=pythonExc.jpg
##file mode=xb
##file is readable=False
##file is writable=True
##file is closed=False
##file is closed=True
##
"""14)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("pythonExc.jpg",mode="rb+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=pythonExc.jpg
##file mode=rb+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
##
"""15)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("bhagavaan.jpg",mode="wb+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##
##file name=pythonnew.jpg
##file mode=rb+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
##
"""16)write a python program on binary files find the given file print the
file name, mode, is readable or not, writable or not and closed or not"""
##f=open("python.jpg",mode="ab+")
##print("file name={}".format(f.name))
##print("file mode={}".format(f.mode))
##print("file is readable={}".format(f.readable()))
##print("file is writable={}".format(f.writable()))
##print("file is closed={}".format(f.closed))
##f.close()
##print("file is closed={}".format(f.closed))
##output:
##file name=python.jpg
##file mode=ab+
##file is readable=True
##file is writable=True
##file is closed=False
##file is closed=True
##
"""17)"""
##import os
##print(os.path.isfile("files.txt"))
##output:
##True
##
##"""18)"""
##import os
##if os.path.isfile("student.txt"):
##    f=open("student.txt")
##    print("file opened")
##    f.close()
##else:
##    print("file is not found")
##output:
##file opened
##
"""19)"""
##
"""20)"""
##
"""21)"""
##
"""22) write a python program on files create a file and store the data"""
##f=open("student4.txt","x")
##f.write("rakesh is a good boy\n")
##f.write("rakesh sits beside me\n")
##f.write("rakesh is learning python\n")
##f.close()
##print("success")
##output:
##success
##
"""23)write a python program on files add some data to the file"""
##f=open("student4.txt","a")
##f.write("he is a good friend of me\n")
##f.write("he always works hard\n")
##f.close()
##print("success")
##output:
##success
##
"""24)write a python program on files store the data list of lines"""
##f=open("student5.txt","w")
##a=["chinny","banny","chunny","vinny"]
##f.writelines(a)
##f.close()
##print("success")
##output:
##success
##chinnybannychunnyvinny
"""25)write a python program on files store the data list of lines"""
##f=open("student5.txt","w")
##a=["chinny\n","bunny\n","sunny\n","vinny\n"]
##f.writelines(a)
##f.close()
##print("success")
##output:
##success
##chinny
##bunny
##sunny
##vinny
##
"""26)write a python program on files add some list of data to the files """
##f=open("student5.txt","a")
##a=["rahul\n","arjun\n","mahesh babu\n"]
##f.writelines(a)
##f.close()
##print("success")
##output:
##success
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
"""27)write a python program on files read the total data from the file"""
##f=open("student5.txt","r")
##data=f.read()
##print(data)
##f.close()
##print("success")
##output:
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
##success
##
"""28) write a python program on files read the data from the file some lines only"""
##f=open("student5.txt","r")
##data1=f.read(2)
##data2=f.read(3)
##print(data1)
##print(data2)
##f.close()
##output:
##ch
##inn
##
"""29)write a python program on files to read the data from the files only 2 lines """
##f=open("student5.txt","r")
##data1=f.readline()
##data2=f.readline()
##print(data1)
##print(data2)
##f.close()
##output:
##chinny
##
##bunny
##
"""30)write a python program on files to read the total data from the file"""
##f=open("student5.txt","r")
##data=f.readlines()
##print(data)
##for i in data:
##    print(i,end="")
##output:
##['chinny\n', 'bunny\n', 'sunny\n', 'vinny\n', 'rahul\n', 'arjun\n', 'mahesh babu\n']
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
"""30)write a python program on files to read the total data from the file"""
##f=open("student5.txt","r")
##data=f.read()
##print(data)
##f.close()
##output:
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
"""31)write a python program on files using tell method"""
##f=open("student5.txt","r")
##print(f.tell())
##print(f.read(5))
##print(f.tell())
##print(f.read(3))
##print(f.tell())
##f.close()
##output:
##0
##chinn
##5
##y
##b
##9
##
"""32)write a python program on files using tell method and seek method"""
##f=open("student5.txt","r")
##print(f.tell())
##print(f.read())
##print(f.seek(5))
##print(f.read())
##print(f.seek(20))
##print(f.read())
##f.close()
##output:
##0
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
##5
##y
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##
##20
##
##vinny
##rahul
##arjun
##mahesh babu
##
##
"""33)write a python on files read and write the data by using tell and seek method"""
##f=open("student5.txt","r+")
##print(f.tell())
##print(f.read())
##print(f.tell())
##f.write("youtube")
##print(f.tell())
##print(f.read())
##print(f.tell())
##f.close()
##output:
##0
##chinny
##bunny
##sunny
##vinny
##rahul
##arjun
##mahesh babu
##youtubeyoutubeyoutube
##77
##84
##
##84
##
"""34)"""
##f=open("student5.txt","w+")
##print(f.tell())
##f.write("youtube")
##print(f.tell())
##print(f.read())
##print(f.tell())
##f.close()
##output:
##0
##7
##
##7
##
"""35)writing and then reading It will overwrite existing data"""
##f=open("studen5.txt","w+")
##print(f.tell())
##f.write("youtube")
##print(f.tell())
##f.seek(0)
##print(f.tell())
##print(f.read())
##print(f.tell())
##f.close()
##output:
##0
##7
##0
##youtube
##7
##
"""36)appending and then reading It wont overwrite existing data"""
##f=open("student5.txt","a+")
##print(f.tell())
##f.write("youtube")
##print(f.tell())
##print(f.read())
##print(f.tell())
##f.close()
##output:
##21
##28
##
##28
##
"""37) Appending and then reading It wont overwrite existing data"""
##f=open("student5.txt","a+")
##print(f.tell())
##f.write("hello")
##f.seek(0)
##print(f.read())
##f.close()
##
##
"""38) copy contents of a file to another file"""
##f1=open("student.txt",mode="r")
##f2=open("student10.txt",mode="w")
##data=f1.read()
##f2.write(data)
##f1.close()
##f2.close()
##print("success")
##output:
##success
##
"""39)with statement"""
##with open("student.txt","r")as f:
##    data=f.read()
##    print(data)
##    print("file is closed={}".format(f.closed))
##print("file is closed={}".format(f.closed))
##output:
##mounika is good girl
##tarak is my another friend
##Youtube
##file is closed=False
##file is closed=True
##
##
"""40) write a python program on files to read total data from the file."""
##f=open("checking_files.txt")
##data=f.read()
##print(data)
##f.close()
##output:
##hi
##hello
##my name is bhagavaan
##i am learning python
##
"""41) write a python program on files to read 10 characters from the file. """
##f=open("checking_files.txt")
##data=f.read(10)
##print(data)
##f.close()
##output:
##hi
##hello
##m
##
"""42)write a python program on files to read 100000 characters from the file."""
##f=open("checking_files.txt")
##data=f.read(100000)
##print(data)
##f.close()
##output:
##hi
##hello
##my name is bhagavaan
##i am learning python
##
"""43)write a python program on files to read -1 characters from the file."""
##f=open("checking_files.txt")
##data=f.read(-1)
##print(data)
##f.close()
##output:
##hi
##hello
##my name is bhagavaan
##i am learning python
"""44) write a python program on files to read all lines line by line data from the file"""
##f=open("checking_files.txt")
##line=f.readline()
##while line !="":
##    print(line,end="")
##    line=f.readline()
##f.close()
##output:
##hi
##hello
##my name is bhagavaan
##i am learning python
##7673956382
##8247468200
##123456789
##987456123
##
"""45) write a python program on files to read all lines into a list"""
##f=open("checking_files.txt")
##l=f.readlines()
##for i in l:
##    print(i,end="")
##f.close()
##output:
##hi
##hello
##my name is bhagavaan
##i am learning python
##7673956382
##8247468200
##123456789
##987456123
##
"""46) write a python program on files to use all methods"""
##f=open("checking_files.txt")
##print(f.read(1))
##print("*"*10)
##print(f.readline())
##print("*"*10)
##print(f.readline())
##print("*"*10)
##print(f.read(4))
##print("*"*10)
##print("remaining total data")
##print(f.read())
##output:
##h
##**********
##i
##
##**********
##hello
##
##**********
##my n
##**********
##remaining total data
##ame is bhagavaan
##i am learning python
##
"""47) write a python program on file to read data from one file and write to another file"""
##f1=open("checking_files.txt")
##f2=open("output.txt","w")
##data=f1.read()
##f2.write(data)
##f1.close()
##f2.close()
##print("data copied from input file to output file successfully")
##output:
##data copied from input file to output file successfully
##
##
"""48)write a python program on files to write the data on file by using with statement"""
##with open("abcdef.txt","w") as f:
##    f.write("hi\n")
##    f.write("hello\n")
##    f.write("my name is bhagavaan\n")
##    f.write("i am in hyderabad\n")
##    print("is file closed={}".format(f.closed))
##print("is file closed={}".format(f.closed))
##output:
##is file closed=False
##is file closed=True
##
##
"""49) write a python program on files to read the data from file by using with statement"""
##with open("abcdef.txt","r") as f1:
##    data=f1.read()
##    print(data)
##    print("is closed={}".format(f1.closed))
##print("is closed={}".format(f1.closed))
####output:
##hi
##hello
##my name is bhagavaan
##i am in hyderabad
##
##is closed=False
##is closed=True
##
"""50)write a python program find the cursor on file"""
##f=open("abcdef.txt","r")
##print(f.tell())
##print(f.read(2))
##print(f.tell())
##print(f.read(3))
##print(f.tell())
##f.close()
##output:
##0
##hi
##2
##
##he
##6
##
"""51) write a python program on files by using tell method and seek methods """
##f=open("abcdef.txt")
##print(f.tell())
##f.seek(3)
##print(f.tell())
##print(f.read(2))
##f.seek(10)
##print(f.read())
##print(f.tell())
##f.seek(0)
##print(f.read())
##f.close()
##output:
##0
##3
##
##h
##
##my name is bhagavaan
##i am in hyderabad
##
##52
##hi
##hello
##my name is bhagavaan
##i am in hyderabad
##
"""52)"""
##f=open("xyz.txt","w")
##f.write("All students are stupids")
##with open("xyz.txt","r+") as f:
##    text=f.read()
##    print("data before modif




"""Exercise questions"""
"""1) Write a program in python to replace all word “the” by another
word “them” in a file “poem.txt”. """
##f=open("checking.txt","w")
##f.write("hi hii how are you")
##f.close()
##f=open("checking.txt","r")
##d=f.read()
##d=d.replace("hii","hello")
##f.close()
##f=open("checking.txt","w")
##f.write(d)
##f.close()

"""2) Write a program in python to replace a character by another character
in a file “story.txt”. (Accept both the characters from the user) """
##f=open("checking.txt","r")
##d=f.read()
##print(d)
##ch=input("Enter character to be replaced=")
##ch1=input("Enter character that will be replaced=")
##data=d.replace(ch,ch1)
##f.close()
##f=open("checking.txt","w")
##f.write(data)
##f.close()

"""3) Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”. """ 
##f=open("checking2.txt","w")
##f.write("""Write a function disp75() in Python to display only
##        those records of students from file “school.dat” who
##        scored more than 75 percent marks. Structure stored in “school.dat”
##        is in the form of list containing information like """)
##f.close()
##f=open("checking2.txt")
##d=f.read()
##d=d.replace("a","@")
##print(d)
##f.close()
##f=open("checking2.txt","w")
##f.write(d)
##f.close()
##output:
##Write @ function disp75() in Python to displ@y only
##        those records of students from file “school.d@t” who
##        scored more th@n 75 percent m@rks. Structure stored in “school.d@t”
##        is in the form of list cont@ining inform@tion like 


"""4) Write a program in python to read file “data.txt” and display only
those lines whose length is more than 40 characters. """
##f=open("dummy3.txt","r")
##d=f.readlines()
##for i in d:
##    if len(i)>40:
##        print(i)
##output:
##Write a function disp75() in Python to display only those records
##
##of students from file “school.dat” who scored more than

"""5) Write a program in python to remove all duplicate lines from the file “story.txt”. """
##f=open("dummy6.txt","w")
##f.write("""hi hi hello hello, my my name name is is bhagavaan bhagavaan
##i i am am learning learning python python hi hi hello hello, my my name name is is bhagavaan bhagavaan
##i i am am learning learning python python""")
##f.close()

##f=open("dummy6.txt","r")
##d=f.readlines()
##m=[]
##for i in d:
##   for j in i:
##       if j not in m:
##           m.append(j)
##print(m)
##f.close()
##output:
##['h', 'i', ' ', 'e', 'l', 'o', ',', 'm', 'y', 'n', 'a', 's', 'b', 'g', 'v', '\n', 'r', 'p', 't']
##f=open("dummy6.txt","w")
##for i in m:
##    f.write(i)
##f.close()
##    

"""6) Write a program in python to display only unique words from the file “story.txt”. """
##f=open("dummy5.txt","r")
##d=f.read()
##e=d.split()
##str=""
##for i in e:
##    if i not in str:
##        str=str+i+" "
##print(str)
##f.close()
##output:
##hi hello hello, my name is bhagavaan learning python

"""7) Write a program in python to count the frequency of each vowels in a file “task.txt”. """
##f=open("dummy5.txt","r")
##d=f.read()
##va=ve=vi=vo=vu=0
##for i in d:
##    if i=="a" or i=="A":
##        va=va+1
##    if i=="e" or i=="E":
##        ve=ve+1
##    if i=="i" or i=="I":
##        vi=vi+1
##    if i=="o" or i=="O":
##        vo=vo+1
##    if i=="u" or i=="U":
##        vu=vu+1
##print("The frequency of a vowel is={}".format(va))
##print("The frequency of e vowel is={}".format(ve))
##print("The frequency of i vowel is={}".format(vi))
##print("The frequency of o vowel is={}".format(vo))
##print("The frequency of u vowel is={}".format(vu))
##output:
##The frequency of a vowel is=14
##The frequency of e vowel is=6
##The frequency of i vowel is=8
##The frequency of o vowel is=4
##The frequency of u vowel is=0

"""8) Write a program in python to count those words whose length is more than
7 characters in a file “story.txt”. """
##f=open("dummy4.txt","r")
##d=f.read()
##e=d.split()
##c=0
##for i in e:
##    if len(i)>7:
##        c=c+1
##print("The words are={}".format(c))
##f.close()
##output:
##The words are=17
        
"""9) Write a program in python to count those lines from the file
“div.txt” which are starting from ‘T’ or ‘M’. """
##f=open("dummy4.txt","r")
##d=f.readlines()
##c=0
##for i in d:
##    if i[0]=="T" or i[0]=="M":
##        c=c+1
##print("The total lines are={}".format(c))
##f.close()
##output:
##The total lines are=1


"""10) Write a program in python to count those lines from the file
“div.txt” which are not starting from ‘M’. """
##f=open("dummy4.txt","r")
##d=f.readlines()
##c=0
##for i in d:
##    if i[0]!="M":
##        c=c+1
##print("The total lines with out starting M={}".format(c))
##f.close()
##output:
##The total lines with out starting M=6


"""11) Write a program in python to display those words from a file
“image.txt” which are ending from alphabet ‘m’. """
##f=open("dummy4.txt","r")
##d=f.read()
##e=d.split()
##c=0
##for i in e:
##    if i[-1]=="M":
##        c=c+1
##print("The total lines are ending with M={}".format(c))
##f.close()
##output:
##The total lines are ending with M=0

"""12) Write a program in python to read all lines of file “data.txt” using readline() only. """
##f=open("dummy4.txt","r")
##str=""
##while str:
##    str=f.readline()
##    print(str,end="")
##f.close()
"""13) Write a program in Python to copy the entire content from file “data.txt” to “story.txt” """
##f1=open("dummy4.txt","r")
##f2=open("dummy7.txt","w")
##d=f1.read()
##f2.write(d)
##print("successfully added")
##f1.close()
##f2.close()
##output:
##successfully added

"""14) Write a program in Python to copy the alternate lines from file “data.txt” to “story.txt """
##f1=open("dummy3.txt","r")
##f2=open("dummy7.txt","w")
##d=f1.readlines()
##for i in range(len(d)):
##    if i%2==0:
##        f2.write(d[i])
##print("successfully added")
##f1.close()
##f2.close()
##output:
##successfully added
        
"""15) Write a program in Python to read the entire content from file “data.txt”
and copy the contents to “story.txt” in upper case.""" 
##f1=open("dummy3.txt","r")
##f2=open("dummy8.txt","w")
##d=f1.readlines()
##for i in d:
##    f2.write(i.upper())
##print("added successfully")
##f1.close()
##f2.close()
##output:
##added successfully

"""16) Write a program in Python to read the entire content from file “data.txt”
and copy only those words to “story.txt” which start from vowels. """
##f1=open("dummy8.txt","r")
##f2=open("dummy10.txt","w")
##d=f1.read()
##e=d.lower()
##f=e.split()
##for i in f:
##    if i[0] in ["a","e","i","o","u"]:
##        f2.write(i)
##print("added successfully")
##f1.close()
##f2.close()
"""17) Write a program in Python to read the entire content from file “data.txt”
and copy only those words in separate lines to “story.txt” which are starting
from lower case alphabets . """
##f1=open("dummy3.txt","r")
##f2=open("dummy11.txt","w")
##d=f1.read()
##word=d.split()
##for i in word:
##    if i[0].islower():
##        f2.write(i)
##        f2.write("\n")
##f1.close()
##f2.close()
        

"""18) Write a program in Python to read file “data.txt” and copy only those
lines to “story.txt” which are starting from alphabets “A” or “T”. """
##f1=open("dummy13.txt","r")
##f2=open("dummy14.txt","w")
##d=f1.readlines()
##print(d)
##for i in d:
##    if i[0]=="A" or i[0]=="T":
##        f2.write(i)
##f1.close()
##f2.close()
"""19) Write a program in Python which display the longest word from file “star.txt” """
##f1=open("checking5.txt","w")
##f1.write("""WRITE
##A FUNCTION
##DISP75()
##IN
##PYTHON
##TO
##DISPLAYJGJPKX
##ONLY
##THOSE
##RECORDS
##OF
##STUDENTS
##FROM
##FILE
##“SCHOOL""")
##f1.close()

##f=open("checking5.txt","r")
##d=f.read()
##l=d.split()
##longword=""
##for i in l:
##    if len(i)>len(longword):
##        longword=i
##print("The long word is={}".format(longword))
##f.close()
##output:
##The long word is=DISPLAYJGJPKX

"""20) Write a program in Python which display the longest line from file “star.txt” """

"""21) Write a program in Python to read the file “star.txt” and display the
entire content after removing leading and trailing spaces. """
##f=open("poem.txt","r")
##d=f.readlines()
##for i in d:
##    print(i.strip())
##f.close()
"""22) Write a program in python that read the content from file
“sumit.txt” and display all numbers. """
##f=open("poem.txt","r")
##d=f.read()
##for i in d:
##    if i.isdigit():
##        print(i)
##f.close()
##output:
##5
##5
##3

"""23) Write a program in Python that display the second and second last line from
the file “life.txt” """
##f=open("poem.txt","r")
##d=f.readlines()
##print("second line is={}".format(d[1]))
##print("second last line is={}".format(d[-2]))
##f.close()

"""24) Consider a binary file “data.dat” which stores the record of “Hotel” in
the form of list containing Room_no, Price, Room_type. Do the following task in a file """

"""a) Write a function addrec() to add a record in a file. """

"""b) Write a function disp() to display all the records from the file. """

"""c) Write a function specific_disp(room_no) which takes room number as argument
and display its details. """

"""d) Write a function mod(room_no) which takes room number as argument
and modify it’s details. """

"""e) Write a function del(room_no) which takes room number as argument
and delete it’s record from file “data.dat” """

"""25) Write a menu driven program which shows all operations on Binary File 

a) Add Record 

b) Display All Record 

c) Display Specific Record 

d) Modify Record 

e) Delete Record 

f) Use “data.dat” file which stores the record of “Hotel” in the form of list
containing Room_no, Price, Room_type """

"""26) Write a function disp75() in Python to display only those
records of students from file “school.dat” who scored more than
75 percent marks. Structure stored in “school.dat” is in the form
of list containing information like [rollno, name, class, percentage]""" 

"""27) Write a function dispname() in Python which will display
only names of all the students from file “school.dat”. Structure
stored in “school.dat” is in the form of list containing information
like [rollno, name, class, percentage]""" 

"""28) Write a function disp12() in Python which will display records
of class 12th students from file “school.dat”. Structure stored in
“school.dat” is in the form of list containing information like
[rollno, name, class, percentage] """

"""29) Write a function search(name) in Python which will display
record of a student from file “school.dat” whose name is passed as
an argument. Structure stored in “school.dat” is in the form of list
containing information like [rollno, name, class, percentage] """

"""30) Write a function disp_mob(model no.) in Python which will display
the record of a mobile from “mobile.dat” whose model number (integer type)
is passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile
brand, Model No., Price] """























