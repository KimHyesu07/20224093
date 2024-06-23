Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> prit"test"
SyntaxError: invalid syntax
>>> prit("test")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    prit("test")
NameError: name 'prit' is not defined. Did you mean: 'print'?
>>> printf("test")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    printf("test")
NameError: name 'printf' is not defined. Did you mean: 'print'?
>>> claer
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    claer
NameError: name 'claer' is not defined
>>> d=1
>>> a=2
>>> a+d
3
>>> print"test"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(test)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(test)
NameError: name 'test' is not defined
>>> print("test")
test
