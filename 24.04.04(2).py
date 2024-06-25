Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> x= [2016, 2017, 2018, 2019,2020]
... y = [350, 410, 520, 695, 543]
... plt.plot(x,y)
... plt.title('Annal sales')
... plt.xlabel('years')
... plt.ylabel('sales')
... plt.show()
