Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world!")
Hello world!
>>> print('Hello world!')
Hello world!
>>> # print("Hello world!")
>>> #print("Γειά σου Κόσμε!")
>>> #print("Olá Mundo!")
>>> #print("Ahoj světe!")
>>> #print("안녕 세상!")
>>> #print("你好，世界!")
>>> #print("नमस्ते दुनिया!")
>>> #print("Salamu, Dunia!")
>>> #print("Merhaba dünya!")
>>> 
====== RESTART: /home/student/derin19_lab3/meet2017y1lab3/HelloWorld.py ======
Merhaba Dünya is how you say Hello World in Turkish.
>>> 
====== RESTART: /home/student/derin19_lab3/meet2017y1lab3/HelloWorld.py ======
Merhaba Dünya is how you say Hello World in Turkish.
Γειά σου Κόσμε is how tou say Hello World in Greek.
>>> 
====== RESTART: /home/student/derin19_lab3/meet2017y1lab3/HelloWorld.py ======
Merhaba Dünya is how you say Hello World in Turkish.
Γειά σου Κόσμε is how you say Hello World in Greek.
Olá Mundo is how you say Hello World in Portugese.
Ahoj světe is how you say Hello World in Czech.
안녕 세상 is how you say Hello World in Korean.
你好，世界 is how you say Hello World in Chinese.
नमस्ते दुनिया is how you say Hello World in Hindi.
Salamu, Dunia is how you say Hello World in Sawahii.
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RobertFrost.py =====
Two roads diverged in a wood, and I-
I took the one less traveled by,
And that has made all the difference.
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RobertFrost.py =====
Two roads diverged in a wood, and I-
I took the one less traveled by,
And that has made all the difference.
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RobertFrost.py =====
Traceback (most recent call last):
  File "/home/student/derin19_lab3/meet2017y1lab3/RobertFrost.py", line 6, in <module>
    print(twoRoads)
NameError: name 'twoRoads' is not defined
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RobertFrost.py =====
Two roads diverged in a wood, and I-
I took the one most traveled by,
And that has made all the difference.
>>> 
>>> "Don't + "forget" + "to" + "conserve" + "water"
SyntaxError: invalid syntax
>>> 'Don't' + 'forget' + 'to' + 'conserve' + 'water'
SyntaxError: invalid syntax
>>> "the"*3
'thethethe'
>>> "the"*3 + "beautiful" + "Earth"
'thethethebeautifulEarth'
>>> 2*"True"
'TrueTrue'
>>> 
>>> a='save'
>>> b='the'
>>> c='planet'
>>> a+b+c
'savetheplanet'
>>> "a "+"b "+"c"
'a b c'
>>> a_+b_+c
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a_+b_+c
NameError: name 'a_' is not defined
>>> a +b +c
'savetheplanet'
>>> a= 'save '
>>> b= 'the '
>>> c= 'planet'
>>> a+b+c
'save the planet'
>>> a= 'save'
>>> b= 'the'
>>> c='planet'
>>> a+ ' '+b+ ' '+c
'save the planet'
>>> a=4
>>> b='panda bears'
>>> a+ b
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a+ b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int(a)+str(b)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(a)+str(b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> int(a) + b
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(a) + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a+ str(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a+ str(b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a) + str(b)
'4panda bears'
>>> str(a)+ ' '+str(b)
'4 panda bears'
>>> x= 'y1 is the best'
>>> len(x)
14
>>> upper(x)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    upper(x)
NameError: name 'upper' is not defined
>>> x.upper()
'Y1 IS THE BEST'
>>> x.lower()
'y1 is the best'
>>> x.capitalize()
'Y1 is the best'
>>> x.swapcase()
'Y1 IS THE BEST'
>>> x.replace('y1','y2')
'y2 is the best'
>>> a='MEET'
>>> b='meet'
>>> c='meat'
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a !=b
True
>>> a!=c
True
>>> b!=c
True
>>> y= 'we are better than the rest'
>>> x==y
False
>>> x!=y
True
>>> len(x)==len(y)
False
>>> z='y2 is the best'
>>> x==y
False
>>> len(x)=len(z)
SyntaxError: can't assign to function call
>>> len(x)==len(y)
False
>>> len9x)==len(z)
SyntaxError: invalid syntax
>>> len(x)==len(z)
True
>>> my_string="bananyellowthinkhatgreyBIGcalifornia314"
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> meet_value= [12,17] + [24,27]
>>> meet_value=[12:17] + [24:27]
SyntaxError: invalid syntax
>>> meet_value[12:17] + [24:27]
SyntaxError: invalid syntax
>>> my_string[12:17] + [24:27]
SyntaxError: invalid syntax
>>> my_string[24:27]
'IGc'
>>> my_string[23:26]
'BIG'
>>> my_string[12:17]
'hinkh'
>>> my_string[11:16]
'think'
>>> my_string[11:16] + [12:17]
SyntaxError: invalid syntax
>>> my_string[11:16] + my_string[12:17]
'thinkhinkh'
>>> my_string[11:16] + ' ' +my_string[23:26]
'think BIG'
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/InputOutput.py =====
How old are you?
16
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/InputOutput.py =====
How old are you?
16
Wow, you're16years old!
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/InputOutput.py =====
How old are you?
16
Wow, you're 16 years old!
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/InputOutput.py =====
How old are you?
16
Wow, you're 16 years old!
How old are you? 16
Wow, you're 16 years old!
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RepeatSongs.py =====
Row your boat
Gently down the stream.
Merrily
Life is but a dream.


And I was like
Baby
oooooooh!
Baby
nooooooo!
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RepeatSongs.py =====
RowRowRow your boat
Gently down the stream.
MerrilyMerrilyMerrily
Life is but a dream.


And I was like
BabyBabyBaby
oooooooh!
BabyBabyBaby
nooooooo!
>>> 
===== RESTART: /home/student/derin19_lab3/meet2017y1lab3/RepeatSongs.py =====
Row Row Row  your boat
Gently down the stream.
Merrily Merrily Merrily 
Life is but a dream.


And I was like
Baby Baby Baby 
oooooooh!
Baby Baby Baby 
nooooooo!
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
16
Traceback (most recent call last):
  File "/home/student/derin19_lab3/meet2017y1lab3/Ages.py", line 6, in <module>
    total(age1+age2)
NameError: name 'total' is not defined
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
16
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
16
1516
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
16
31
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
14
29
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
14
29
False
>>> 
========= RESTART: /home/student/derin19_lab3/meet2017y1lab3/Ages.py =========
How old are you student 1 ?
15
WoW student 1!!
And how old are you student 2 ?
14
29
your ages arent the same
True
>>> 
==== RESTART: /home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py ====
What is your name?
derin
Traceback (most recent call last):
  File "/home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py", line 3, in <module>
    print(name + "can't wait to start writing harder programs!")
NameError: name 'name' is not defined
>>> 
==== RESTART: /home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py ====
What is your name?
derin
Traceback (most recent call last):
  File "/home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py", line 3, in <module>
    print(name + "can't wait to start writing harder programs!")
NameError: name 'name' is not defined
>>> 
==== RESTART: /home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py ====
What is your name?
derin
derincan't wait to start writing harder programs!
Who is your favorite instructor?

==== RESTART: /home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py ====
What is your name?
derin
derin can't wait to start writing harder programs!
Who is your favorite instructor?
adam
My favorite instructor is adam and he is AWESOME.
Which team are you on?
y1
y1 is the best team in all of MEET
>>> 
==== RESTART: /home/student/derin19_lab3/meet2017y1lab3/Badbadbadcode.py ====
What is your name?
derin
derin can't wait to start writing harder programs!
Who is your favorite instructor?
adam
My favorite instructor is adam and he is AWESOME.
Which team are you on?
y1
y1 is the best team in all of MEET
>>> 
