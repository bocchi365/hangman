Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.pow(2,3)
8.0
>>> math.pow(3,6)
729.0
>>> import random
>>> random.randint(0,100)
51
>>> random.randint(0,200)
102
>>> random.randint(0,9999)
2407
>>> nums=[1,5,3,,12,46,33,2]
SyntaxError: invalid syntax
>>> nums=[1,5,3,12,46,33,2]
>>> import statistics
>>> statistics.mean(nums)
14.571428571428571
>>> mean(nums)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mean(nums)
NameError: name 'mean' is not defined
>>> statistics.median(nums)
5
>>> statistics.mode(nums)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    statistics.mode(nums)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/statistics.py", line 506, in mode
    'no unique mode; found %d equally common values' % len(table)
statistics.StatisticsError: no unique mode; found 7 equally common values
>>> statistics.mode(nums)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    statistics.mode(nums)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/statistics.py", line 506, in mode
    'no unique mode; found %d equally common values' % len(table)
statistics.StatisticsError: no unique mode; found 7 equally common values
>>> nums[1,5,33,12,46,33,2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nums[1,5,33,12,46,33,2]
TypeError: list indices must be integers or slices, not tuple
>>> nums=[1,5,33,12,46,33,2]
>>> statistics.mode(nums)
33
>>> import keyword
>>> keyword.iskeyword("for")
True
>>> keyword.iskeyword("football")
False
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/project.py =============
Hello
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module2.py =============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/module2.py", line 1, in <module>
    import module1
  File "/Users/reimurakoshi/Desktop/練習/module1.py", line 1
    print("Hello")
    ^
IndentationError: unexpected indent
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module2.py =============
Hello
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module2.py =============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/module2.py", line 1, in <module>
    import module1
  File "/Users/reimurakoshi/Desktop/練習/module1.py", line 1
    if_name_=="_main_":
                      ^
SyntaxError: invalid syntax
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module2.py =============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/module2.py", line 1, in <module>
    import module1
  File "/Users/reimurakoshi/Desktop/練習/module1.py", line 1
    if_name_=="_main_":
                      ^
SyntaxError: invalid syntax
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module1.py =============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/module1.py", line 1, in <module>
    if _name_=="_main_" :
NameError: name '_name_' is not defined
>>> 
============= RESTART: /Users/reimurakoshi/Desktop/練習/module1.py =============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/module1.py", line 1, in <module>
    if _name_ == "_main_" :
NameError: name '_name_' is not defined
>>> import os
>>> os.path.join("練習","module1.py")
'練習/module1.py'
>>> st=open("st.txt","w")
>>> st.write("Hi from Python")
14
>>> st.close()
>>> st=open("st.txt","w",encodint="utf-8")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    st=open("st.txt","w",encodint="utf-8")
TypeError: 'encodint' is an invalid keyword argument for open()
>>> st=open("st.txt","w",encoding="utf-8")
>>> st.write("Pythonからこんにちは")
13
>>> st.close
<built-in method close of _io.TextIOWrapper object at 0x103e12708>
>>> st.close()
>>> with open("st.txt","w") as f:
	f.write("Hi from Python")

	
14
>>> with open("st.txt","r") as f:
	print(f.read())

	
Hi from Python
>>> with open("st.txt","w") as f:
	f.write("hello this is rei murakoshi. Nice to me too")

	
43
>>> with open("st.txt","r") as f:
	print(f.read())

	
hello this is rei murakoshi. Nice to me too
>>> with open("st.txt","r",encoding="utf-8") as f:
	print(f.read())

	
hello this is rei murakoshi. Nice to me too
>>> my_list=[]
>>> with open("st.txt","r") as f:
	my_list.append(f.read())

	
>>> print(my_list)
['hello this is rei murakoshi. Nice to me too']
>>> import csv
>>> with open("st.csv","w",newline=") as f:
	      
SyntaxError: EOL while scanning string literal
>>> with open("st.csv","w",newline='') as f:
	      w=csv.writer(f,delimiter=",")
	      w.writerow(["one","two","three"])
	      w.writerwor(["four","five","six"])

	      
15
Traceback (most recent call last):
  File "<pyshell#57>", line 4, in <module>
    w.writerwor(["four","five","six"])
AttributeError: '_csv.writer' object has no attribute 'writerwor'
>>> >>> with open("st.csv","w",newline='') as f:
	      w=csv.writer(f,delimiter=",")
	      w.writerow(["one","two","three"])
	      
SyntaxError: invalid syntax
>>> >>> with open("st.csv","w",newline='') as f:
	      w=csv.writer(f,delimiter=",")
	      w.writerow(["one","two","three"])
	      
SyntaxError: invalid syntax
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 6, in <module>
    w.write.row(["four","five","six"])
AttributeError: '_csv.writer' object has no attribute 'write'
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 8, in <module>
    print(os.getcwd())
NameError: name 'os' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 8, in <module>
    print(os.getcwd(st.csv))
NameError: name 'os' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 8, in <module>
    print(os.getcwd("st.csv"))
NameError: name 'os' is not defined
>>> import csv
	      
>>> with open("st.csv","r") as f :
	      r=csv.reader(f,delimiter=",")
	      for row in r:
		      print(",".join(row))

	      
one,two,three
four,five,six
>>> import os
	      
>>> path=os.getcwd()
	      
>>> print(path)
	      
/Users/reimurakoshi/Desktop/練習
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 18, in <module>
    while wrong<len(stages)-1:
NameError: name 'wrong' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 18, in <module>
    while wrong<len(stages) -1 :
NameError: name 'wrong' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 18, in <module>
    while wrong < len(stages) - 1 :
NameError: name 'wrong' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
>>> word
	      
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    word
NameError: name 'word' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 41, in <module>
    hangman("cat")
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 13, in hangman
    board["_"]*len(word)
NameError: name 'board' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
ハングマンへようこそ!!!


Traceback (most recent call last):
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 41, in <module>
    hangman("cat")
  File "/Users/reimurakoshi/Desktop/練習/st.py", line 21, in hangman
    char=imput(msg)
NameError: name 'imput' is not defined
>>> 
=============== RESTART: /Users/reimurakoshi/Desktop/練習/st.py ===============
ハングマンへようこそ!!!


Please predict one characterd
_ _ _

_______          


Please predict one characteri
_ _ _

_______          
|                


Please predict one characteri
_ _ _

_______          
|                
|      |         


Please predict one characteri
_ _ _

_______          
|                
|      |         
|      o         


Please predict one characterk
_ _ _

_______          
|                
|      |         
|      o         
|     /|\        


Please predict one characterk
_ _ _

_______          
|                
|      |         
|      o         
|     /|\        
|     / \        


Please predict one characterk
_ _ _

_______          
|                
|      |         
|      o         
|     /|\        
|     / \        
|                

_______          
|                
|      |         
|      o         
|     /|\        
|     / \        
|                
あなたの負け。正解はcat.
>>> k
	      
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    k
NameError: name 'k' is not defined
>>> 
