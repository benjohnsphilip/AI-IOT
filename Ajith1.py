Python 3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x=10
>>> y=20
>>> x+y
30
>>> x=2.6
>>> f=33
>>> x+f
35.6
>>> x+f
35.6
>>> y+f
53
>>> x=3.0
>>> y=20
>>> x+y
23.0
>>> print(x)
3.0
>>> print9y)
SyntaxError: invalid syntax
>>> print(y)
20
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> print('ajith')
ajith
>>> x='india'
>>> print(x)
india
>>> y='is'
>>> z='my contry'
>>> print(x+y+z)
indiaismy contry
>>> x+" "+y+" "
'india is '
>>> x+" "+y+" "+z
'india is my contry'
>>> x
'india'
>>> x+y
'indiais'
>>> x+" "+y
'india is'
>>> x='india'
>>> len(x)
5
>>> 3+2j
(3+2j)
>>> (3+2j)*(2+3j)
13j
>>> j*j
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    j*j
NameError: name 'j' is not defined
>>> 1j*1j
(-1+0j)
>>> 1j*1j*1j
(-0-1j)
>>> 1j*1j*1j*1j
(1-0j)
>>> sin(1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    sin(1)
NameError: name 'sin' is not defined
>>> 
>>> x='india'
>>> x[0}
SyntaxError: invalid syntax
>>> x[0]
'i'
>>> x[1]
'n'
>>> x[5]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    x[5]
IndexError: string index out of range
>>> x[4]
'a'
>>> x[1:4]
'ndi'
>>> x[0]+x[1:4]+x[4]
'india'
>>> for a in range(10):
	print(a)

	
0
1
2
3
4
5
6
7
8
9
>>> range(10)
range(0, 10)
>>> x=range(10)
>>> x
range(0, 10)
>>> print(x)
range(0, 10)
>>> x='india'
>>> for x in range(4)
SyntaxError: invalid syntax
>>> for x in range(4):
	print(x)

	
0
1
2
3
>>> x='india'
>>> for a in x
SyntaxError: invalid syntax
>>> for a in x:
	print(a)

	
i
n
d
i
a
>>> 
>>> x='india'
>>> x.upper()
'INDIA'
>>> x.lower()
'india'
>>> x.strip()
'india'
>>> x.serch("i")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    x.serch("i")
AttributeError: 'str' object has no attribute 'serch'
>>> x.find("1")
-1
>>> x.find("d")
2
>>> x.find("i"0
       
SyntaxError: invalid syntax
>>> x.find("i")
0
>>> x[-1]
'a'
>>> x[-2]
'i'
>>> x.replace("d","c")
'incia'
>>> x=10
>>> float(x)
10.0
>>> x=10.5
>>> int(x)
10
>>> x=10
>>> if x==11:
	print("x=11")

	
>>> if (x==11):
	print("x=11")
    if (x==10)
    
SyntaxError: unindent does not match any outer indentation level
>>> if (x==11):
	print("x=11")
    if (x==10):
	    
SyntaxError: unindent does not match any outer indentation level
>>> if (x==11):
	print("x=11")
    if (x==10)
