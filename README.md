# Benny Language 
base on Python 3
Lua like Class object variable system on Python 

Benny 0.91
==========

to test

python benny.py

What is Class object variable?
==============================
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

Benny error more than [1 block] in sentense

You can do like this

a.b[x=100,y=200]

a.b.c[x=150,y=250]

Seperate into 2 lines

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
