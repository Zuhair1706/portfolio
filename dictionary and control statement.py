Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#DICTIONARY::
# OBJECTS ARE REPRESENTED AS KEY-VALUE PAIRS
#TO DECLARE A LIST THE SYNTAX IS :
DICT_NAME={'NAME':'ZUHAIR'
           'AGE':'19'
           'DOB':'170605'}
SyntaxError: invalid syntax
DICT_NAME={'NAME':'ZUHAIR','AGE':19,'DOB':170605}
DICT_NAME
{'NAME': 'ZUHAIR', 'AGE': 19, 'DOB': 170605}
DICT_NAME.values('NAME')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    DICT_NAME.values('NAME')
TypeError: dict.values() takes no arguments (1 given)
DICT_NAME.calues()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    DICT_NAME.calues()
AttributeError: 'dict' object has no attribute 'calues'. Did you mean: 'values'?
DICT_NAME.values()
dict_values(['ZUHAIR', 19, 170605])
DICT_NAME.get(AGE)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    DICT_NAME.get(AGE)
NameError: name 'AGE' is not defined
DICT
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    DICT
NameError: name 'DICT' is not defined
DICT_NAME.get('AGE')
19
DICT_NAME.get('NAME')
'ZUHAIR'
DICT_NAME.items()
dict_items([('NAME', 'ZUHAIR'), ('AGE', 19), ('DOB', 170605)])
DICT_NAME.keys()
dict_keys(['NAME', 'AGE', 'DOB'])
DICT_NAME.popitem()
('DOB', 170605)
DICT_NAME
{'NAME': 'ZUHAIR', 'AGE': 19}
DICT_NAME.pop('AGE')
19
DICT_NAME
{'NAME': 'ZUHAIR'}
DICT_2={'name':kyz,'ghy':pop23}
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    DICT_2={'name':kyz,'ghy':pop23}
NameError: name 'kyz' is not defined
DICT_2={'name':'kyz','ghy':'pop23'}
DICT_NAME.fromkeys(DICT_2)
{'name': None, 'ghy': None}
DICT_NAME
{'NAME': 'ZUHAIR'}
DICT_NAME.update(Dict_2)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    DICT_NAME.update(Dict_2)
NameError: name 'Dict_2' is not defined. Did you mean: 'DICT_2'?
DICT_NAME.update(DICT_2)
DICT_NAME
{'NAME': 'ZUHAIR', 'name': 'kyz', 'ghy': 'pop23'}
# it does not support duplicate values
DICT_NAME.setdefault('name')
'kyz'
DICT_NAME
{'NAME': 'ZUHAIR', 'name': 'kyz', 'ghy': 'pop23'}
{'NAME': 'ZUHAIR', 'name': 'kyz', 'ghy': 'pop23'}
{'NAME': 'ZUHAIR', 'name': 'kyz', 'ghy': 'pop23'}



diction={'one':'un','two':'dos','three':'tres'}
diction.setdefault('one')
'un'
diction.clear()
diction
{}
# to make changes in a particular key value , create a new dictionary with the required specifications and then use update method to change the values.it wont happen if  the key is setdefault
x=DICT_NAME.setdefault(['name':'dsk'])
SyntaxError: invalid syntax
x=DICT_NAME.setdefault('name':'dsk')
SyntaxError: invalid syntax
x=DICT_NAME.setdefault('nname','dsh')
print(x)
dsh
DICT_NAME
{'NAME': 'ZUHAIR', 'name': 'kyz', 'ghy': 'pop23', 'nname': 'dsh'}
x=DICT_NAME.setdefault('name','dsk')
x
'kyz'
# type conversion

'''same as type casting'''
'same as type casting'
''' we can convert one type of variabe to another datatype. this is called type casting ot type conversion. there are tew types of casting . implicit and explicit.
implicit ==> done by compiler/interpreter(pre-defined)
explicit==> done by user  (user -defined)
'''
' we can convert one type of variabe to another datatype. this is called type casting ot type conversion. there are tew types of casting . implicit and explicit.\nimplicit ==> done by compiler/interpreter(pre-defined)\nexplicit==> done by user  (user -defined)\n'
pi=3.14
num=int(pi)
num
3
type(num)
<class 'int'>
flag = True
c=int(flag)
c
1
# the default value of 0 is always is false while that of there numbers is 1
mink=-0
int(mink)
0
print(bi(2))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(bi(2))
NameError: name 'bi' is not defined. Did you mean: 'pi'?
binary(2)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    binary(2)
NameError: name 'binary' is not defined
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

flo = 5.90
print(int(flo))
5
type(flo)
<class 'float'>
cmplx=3+5j
type(cmplx)
<class 'complex'>
>>> v = int(cmplx)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    v = int(cmplx)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> v= str(cmplx)
>>> print(type(v))
<class 'str'>
>>> w=str(3+5j)
>>> w
'(3+5j)'
>>> f=int(w)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    f=int(w)
ValueError: invalid literal for int() with base 10: '(3+5j)'
>>> cmplx=3+5j
... type(cmplx)
SyntaxError: multiple statements found while compiling a single statement
>>> plx=4+5j
>>> type(plx)
<class 'complex'>
>>> int(plx)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(plx)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> u=str(plx)
>>> u
'(4+5j)'
>>> # control flow statements::::
>>> # if statemenr
>>> # if-else
>>> #if-else-elif
>>> #nested if
>>> age=19
>>> if(age>=18):
...     print('YOUM ARE ELIGIBLE FOR VOTING')
... 
YOUM ARE ELIGIBLE FOR VOTING
>>> A=8
>>> if(A%2==1):
...     print("true")
... 
...     
