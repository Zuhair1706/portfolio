Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1)
list1=[0,1,2,3,4,5,6,7,8,9,10]
list1.reverse()
print(list1)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#2)
list2=[11,12,13,14,15]
list1.append([list2])
list1.append([list2])=c
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
list3=list1.append([list2])
print(list3)
None
list1.extend(0,list2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list1.extend(0,list2)
TypeError: list.extend() takes exactly one argument (2 given)
list1.append(0,list2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1.append(0,list2)
TypeError: list.append() takes exactly one argument (2 given)
d=list1+list2
print(d)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, [[11, 12, 13, 14, 15]], [[11, 12, 13, 14, 15]], 11, 12, 13, 14, 15]
#3)
list4=[0,2,4,6,8,10]
for i in list4:
    print(i*i)

0
4
16
36
64
100
list4=[0,2,4,6,8,10]
for i in list4:
    print([i*i])
    
SyntaxError: multiple statements found while compiling a single statement
squarelist=[i*i for i in list4]
print(squarelist)
[0, 4, 16, 36, 64, 100]
#5)
stlist=['','INDIA','','USA','UK']
stlist.remove('')
stlist
['INDIA', '', 'USA', 'UK']
stlist.remove('')
stlist
['INDIA', 'USA', 'UK']
#6)
stlist
['INDIA', 'USA', 'UK']
stlist.insert(2,'UAE')
stlist
['INDIA', 'USA', 'UAE', 'UK']
#7)
eurolist=['spain','italy','france','germany']
eurolist.insert(3,stlist)
>>> eurolist
['spain', 'italy', 'france', ['INDIA', 'USA', 'UAE', 'UK'], 'germany']
>>> salist['brazil','argentina']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    salist['brazil','argentina']
NameError: name 'salist' is not defined. Did you mean: 'stlist'?
>>> eurolist.append(salist)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    eurolist.append(salist)
NameError: name 'salist' is not defined. Did you mean: 'stlist'?
>>> salist['brazil','argentina']
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    salist['brazil','argentina']
NameError: name 'salist' is not defined. Did you mean: 'stlist'?
>>> eurolist.append([1,2,3,4,5])
>>> eurolist
['spain', 'italy', 'france', ['INDIA', 'USA', 'UAE', 'UK'], 'germany', [1, 2, 3, 4, 5]]
>>> #8)
>>> eurolist.pop()
[1, 2, 3, 4, 5]
>>> eurolist.append[6,7,8,9,10])
SyntaxError: unmatched ')'
>>> 
>>> eurolist.append([6,7,8,9])
>>> eurolist
['spain', 'italy', 'france', ['INDIA', 'USA', 'UAE', 'UK'], 'germany', [6, 7, 8, 9]]
>>> #9)
>>> new=[0,2,0,3,0,5,0,7,0,9]
>>> new.remove('0')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    new.remove('0')
ValueError: list.remove(x): x not in list
>>> new.remove(0)
>>> new
[2, 0, 3, 0, 5, 0, 7, 0, 9]
>>> for i in new:
...     if i==0:
...         new.remove(i)
... 
...         
>>> new
[2, 3, 5, 7, 9]
