# NiceHexSpiral.py
from turtle import *
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
bgcolor('black')
speed(0)
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    fd(x)
    left(59)

done()