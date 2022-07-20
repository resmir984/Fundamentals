#Frontend:html,css,bootstrap,javascript
#Backend: python,django,mysql,api[django rest framework]
#vcs git and github

#coding standards
#======================

#1. snake case
#2. camel case
#3. pascal case

#name
#variable name (snake case follow)

#function name  (snake case follow)
#class name  (pascal case follow)

#def printValue(): not
#def print_value(): correct

#class Person: correct
#class person:not

#class Person_details:not
#class PersonDetails: correct(pascal)

#first_name="ram": correct
#firstName="ram": not

def add(n1,n2):
    return n1+n2

def add(n1,n2,n3):
    return n1+n2+n3

def add(n1,n2,n3,n4):
    return n1+n2+n3+n4

def add(*args):#[10,20,30,40]
    print(args)
add(10,20,30)

def add(*args):#(10,20,30,40)
    return sum(args)
print(add(10,20,30))

def print_details(*args):
    print(args[0])
    print(args[1])
    print(args[2])
print_details("hari","thrissur","kakkanad")

def print_details(*args,**kwargs):
    print(kwargs)
print_details(name="hari",n_place="thrissur",w_loc="kakkanad")

