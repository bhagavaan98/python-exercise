"""1.Write a Python program to read last n lines of a file."""
##def read_lastlines(filename,n):
##    with open(filename,"r") as f:
##        for i in (f.readlines() [-n:]):
##            print(i)
##n=int(input("Enter any number="))
##read_lastlines("dummy3.txt",n)
####output:
##Enter any number=4
##list 
##
##Containing
##
##information
##
##Like

"""2.Write a Python program to read a file line by line and store it into a list."""
##with open("student.txt") as f:
##    content=f.readlines()
##    for i in content:
##        print ([i])
##output:
##['hello\n']
##['hi\n']
##['hiii\n']
##['how are you']

"""3.Write a Python program to read a file line by line store it into a variable."""
##def store_into_variable(filename):
##    with open(filename,"r") as f:
##        variable=f.readlines()
##        print(variable)
##store_into_variable("student.txt")
##output:
##['hello\n', 'hi\n', 'hiii\n', 'how are you']

"""4. Write a Python program to count the frequency of words in a file"""
##from collections import Counter
##with open("student.txt","r") as f:
##    data=Counter(f.read().split())
##    print(data)
##output:
##Counter({'hello': 1, 'hi': 1, 'hiii': 1, 'how': 1, 'are': 1, 'you': 1})
    
"""5. Write a Python program to read a random line from a file."""
##from random import choice
##with open("student.txt") as f:
##    data=f.read().splitlines()
##    print(choice(data))
##output:
##hi
##output:
##hello

"""6.Write a Python program to generate 26 text files named
A.txt, B.txt, and so on up to Z.txt."""
##for i in range(65,65+26):
##    filename=chr(i)+".txt"
##    with open(chr(i)+".txt","w") as file:
##        file.writelines(chr(i))

"""7.Write a Python program to extract characters from
various text files and puts them into a list."""
##import glob
##char_list=[]
##files_list=glob.glob("*.txt")
##for i in files_list:
##    with open(i,"r") as f:
##        char_list.append(f.read())
##print(char_list)
"""8.Write a Python program that takes a text file as input
and returns the number of words of a given text file
Note: Some words can be separated by a comma with no space."""
##with open("student.txt") as f:
##    data=f.read()
##    result=data.replace(","," ")
##    print(result)
##    print(len(result.split()))
##
####output:
##hello 
##hi
##hiii  
##how are you
##6

"""9.Write a Python program to create a file where all letters
of English alphabet are listed by specified number of letters on each line"""
##n=int(input("Enter the number of characters in a line you want="))
##alphabets=""
##for i in range(65,65+26):
##    charvalue=chr(i)
##    alphabets=alphabets+charvalue
##with open("dummy14.txt","w") as f:
##    modification=[alphabets[i:i+n]+"\n" for i in range(0,len(alphabets),n)]
##    f.writelines(modification)
##output:
##Enter the number of characters in a line you want=5
##ABCDE
##FGHIJ
##KLMNO
##PQRST
##UVWXY
##Z


        














