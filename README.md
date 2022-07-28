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



a.b[pos={"x":100,"y":200}] --- dict not allow in Benny

Benny error more than [1 block] in sentense and dict not allow

![Benny](https://github.com/homegardencontrol/benny/blob/main/benny.png?raw=true)

Something need in code
======================

How to get Benny Class object variable from variable string ?

a.b.c[x=100,y=200]

exec('value = a.b.c.x')

or

sometext = 'x'

exec('value = a.b.c.'+sometext)

print(value)

100
