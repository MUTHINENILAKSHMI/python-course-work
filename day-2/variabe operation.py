Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================================================== RESTART: C:/Users/LAKSHMI/OneDrive/Desktop/python-course-work/day-2/Day-2.py =====================================================
Traceback (most recent call last):
  File "C:/Users/LAKSHMI/OneDrive/Desktop/python-course-work/day-2/Day-2.py", line 3, in <module>
    print(keyword.kwlist())
TypeError: 'list' object is not callable
>>> 
===================================================== RESTART: C:/Users/LAKSHMI/OneDrive/Desktop/python-course-work/day-2/Day-2.py =====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=10
>>> b=20
>>> a=10,20,30
>>> a
(10, 20, 30)
>>> b
20
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=10
>>> a,b=b,a
>>> a
20
>>> b
10
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
