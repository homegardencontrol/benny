# Benny Language 
base on Python 3
Lua like Class object variable system on Python 

Benny 0.91
==========

to test

python benny.py

What is Class object variable?
==============================
![Benny Language](https://github.com/homegardencontrol/benny/blob/main/benny_language.png?raw=true)

examples
========
a.b.c.x=100

or

a.b.c[x=100,y=200]

check

print(a.b.c.x)

100

print(a.b.c.y)

200

Don't do this
=============
a.b[x=100,y=200,c[x=150,y=250]]

Benny error more than [1 block] in sentense and dict not allow

You can do like this

a.b[x=100,y=200]

a.b.c[x=150,y=250]

Seperate into 2 lines

Dict not allow but array can
============================

a.b[pos={"x":100,"y":200}] --- dict not allow in Benny

Benny error more than [1 block] in sentense and dict not allow

a.b.varray = [0,1,2,3,4,5] 

print(a.b.varray)

{0,1,2,3,4,5}

![Benny](https://github.com/homegardencontrol/benny/blob/main/benny_function.png?raw=true)

Something need in code
======================

Dict not allow, How to get Benny Class object variable from variable string ?

a.b.c[x=100,y=110]

x = benny('a.b.c.x')

or

sometext = 'x'

x = benny('a.b.c.'+sometext)

print(x)

100

Benny in function
=================

![Benny in function](https://github.com/homegardencontrol/benny/blob/main/benny_in_def.png?raw=true)
