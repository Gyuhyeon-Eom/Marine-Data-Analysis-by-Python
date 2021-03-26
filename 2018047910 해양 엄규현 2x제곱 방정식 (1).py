Python 3.7.0b3 (v3.7.0b3:4e7efa9c6f, Mar 29 2018, 18:42:04) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from mathe import
SyntaxError: invalid syntax
>>> from math import *
>>> for in range(1,21)
SyntaxError: invalid syntax
>>> for I in range(1,21) :
	print("%d의 제곱근은 %.3f입니다."%(I, sqrt(I)))

	
1의 제곱근은 1.000입니다.
2의 제곱근은 1.414입니다.
3의 제곱근은 1.732입니다.
4의 제곱근은 2.000입니다.
5의 제곱근은 2.236입니다.
6의 제곱근은 2.449입니다.
7의 제곱근은 2.646입니다.
8의 제곱근은 2.828입니다.
9의 제곱근은 3.000입니다.
10의 제곱근은 3.162입니다.
11의 제곱근은 3.317입니다.
12의 제곱근은 3.464입니다.
13의 제곱근은 3.606입니다.
14의 제곱근은 3.742입니다.
15의 제곱근은 3.873입니다.
16의 제곱근은 4.000입니다.
17의 제곱근은 4.123입니다.
18의 제곱근은 4.243입니다.
19의 제곱근은 4.359입니다.
20의 제곱근은 4.472입니다.
>>> from math import
SyntaxError: invalid syntax
>>> from math import *
>>> for I in range(1,21)
SyntaxError: invalid syntax
>>> 
>>> 
>>> from math import *
>>> for I in range(1,21):
	print("%d의 제곱근은 %.4f입니다."%(I, sqrt(I)))

	
1의 제곱근은 1.0000입니다.
2의 제곱근은 1.4142입니다.
3의 제곱근은 1.7321입니다.
4의 제곱근은 2.0000입니다.
5의 제곱근은 2.2361입니다.
6의 제곱근은 2.4495입니다.
7의 제곱근은 2.6458입니다.
8의 제곱근은 2.8284입니다.
9의 제곱근은 3.0000입니다.
10의 제곱근은 3.1623입니다.
11의 제곱근은 3.3166입니다.
12의 제곱근은 3.4641입니다.
13의 제곱근은 3.6056입니다.
14의 제곱근은 3.7417입니다.
15의 제곱근은 3.8730입니다.
16의 제곱근은 4.0000입니다.
17의 제곱근은 4.1231입니다.
18의 제곱근은 4.2426입니다.
19의 제곱근은 4.3589입니다.
20의 제곱근은 4.4721입니다.
>>> from random import *
>>> for I in range(6):
	print("%d의 숫자는 : %d입니다."%(I+1,randint(1,45)))

	
1의 숫자는 : 9입니다.
2의 숫자는 : 23입니다.
3의 숫자는 : 45입니다.
4의 숫자는 : 25입니다.
5의 숫자는 : 24입니다.
6의 숫자는 : 26입니다.
>>> 
>>> from random import *

for I in range(6):
	print("%d의 숫자는 : %d입니다."%(I+1,randint(1,45)))
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import turtle
>>> turtle.forward(15)
>>> turtle.forward(100)
>>> turtle.forward(90)
>>> turtle.forward(40)
>>> trutle.right(20)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    trutle.right(20)
NameError: name 'trutle' is not defined
>>> turtle.right(20)
>>> turtle.circle(100)
>>> import. turtle as tt
SyntaxError: invalid syntax
>>> import turtle as tt
>>> tt. right(123)
>>> tt.right(90)
>>> tt,forwad(100)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    tt,forwad(100)
NameError: name 'forwad' is not defined
>>> tt.forward(100)
>>> i=100
>>> while i>2:
	tt.circle(i)

	
Traceback (most recent call last):
  File "<string>", line 8, in circle
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 3182, in _goto
    fill="", width=self._pensize)
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 545, in _drawline
    self.cv.coords(lineitem, *cl)
  File "<string>", line 1, in coords
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 2466, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    tt.circle(i)
  File "<string>", line 12, in circle
turtle.Terminator
reset()

import turtle
reset()
tt.reset()
tt.home()
tt.stop()
>>> import tt
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    import tt
ModuleNotFoundError: No module named 'tt'
>>> import turtle
>>> turtle. fd(100)
>>> import turtle as t
>>> t.bk(21)
>>> t.bk(20)
>>> t.right(20)
>>> t.fd(30)
>>> t.goto(20.30)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t.goto(20.30)
  File "<string>", line 8, in goto
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1774, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be an iterable, not float
>>> t.goto(300,300)
>>> t.setx(20)
>>> t.sety(30)
>>> t.circle(20)
>>> t.heading
<function heading at 0x00000169EA31DE18>
>>> t.distance(200.430)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t.distance(200.430)
  File "<string>", line 8, in distance
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1858, in distance
    return abs(pos - self._position)
UnboundLocalError: local variable 'pos' referenced before assignment
>>> t.distance(20.24)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    t.distance(20.24)
  File "<string>", line 8, in distance
  File "C:\Users\PC-23\AppData\Local\Programs\Python\Python37\lib\turtle.py", line 1858, in distance
    return abs(pos - self._position)
UnboundLocalError: local variable 'pos' referenced before assignment
>>> t.pu()
>>> t.color('blue')
>>> t.begin_fill()
>>> onclick(10.1x**2+`105x+32)
SyntaxError: invalid syntax
>>> onclick(10.1 x**2+`105x+32)
SyntaxError: invalid syntax
>>> import x
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import x
ModuleNotFoundError: No module named 'x'
>>> x_min = -5
>>> x_max = +5
>>> y_min = -5
>>> y_max = +5
>>> space = 0.01
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)

		
Traceback (most recent call last):
  File "<pyshell#96>", line 3, in <module>
    exec(func)
  File "<string>", line 1
    y = -2x*x+13x+2
          ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x_min = -5
>>> x_max = +5
>>> y_min = -5
>>> y_max = +5
>>> space = 0.01
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)
		
SyntaxError: multiple statements found while compiling a single statement
>>> x_min = -5:
>>> x_max = +5:
>>> y_min = -5:
>>> y_max = +5:
>>> space = 0.01:
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)
		
SyntaxError: invalid syntax
>>> x_min = -5
>>> x_max = +5
>>> y_min = -5
>>> y_max = +5
>>> space = 0.01
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)
		
SyntaxError: multiple statements found while compiling a single statement
>>> x_min = -5
>>> x_max = +5
>>> y_min = -5
>>> y_max = +5
>>> space = 0.01
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)
		
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> x_min = -5
>>> x_max = +5
>>> y_min = -5
>>> y_max = +5
>>> space = 0.01
>>> func_list = ["y = -2x*x+13x+2"]
>>> t.setworldcoordinates(x_min.y_min,x_max,y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.setworldcoordinates(x_min. y_min, x_max, y_max)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    t.setworldcoordinates(x_min. y_min, x_max, y_max)
AttributeError: 'int' object has no attribute 'y_min'
>>> t.speed(10)
>>> t.pensize(2)
>>> t.goto(x_min, 0)
>>> t.down()
>>> t.goto(x_max,0)
>>> t. up()
>>> t. goto(0, y_min)
>>> t. down()
>>> t. goto(0, y,max)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t. goto(0, y,max)
NameError: name 'y' is not defined
>>> t. goto(0, y_max)
>>> t.color("black")
>>> for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x,y)
	t.down()
	while x <= x_max:
		x= x+space
		exec(func)
		t.goto(x,y)
		
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> import turtle as t
>>> space = 0.1
>>> func_list = ["y=-2x*x"]
>>> t. speed(2)
>>> t. pensize(2)
>>> t.up()
>>> t.goto(x, 0)
>>> t.down()
>>> t.up()
>>> t.goto(0,y)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    t.goto(0,y)
NameError: name 'y' is not defined
>>> 
>>> t.clearscreen()
>>> 
import turtle
import math

myPen = turtle.Turtle()
myPen.speed(0)

screen = turtle.Screen()
screen.bgcolor("#000000")


def drawAxis():
 
  myPen.penup()
  myPen.goto(-200,0)
  myPen.pendown()
  myPen.goto(200,0)
 
  myPen.penup()
  myPen.goto(0,-200)
  myPen.pendown()
  myPen.goto(0,200)
  

def drawLine(a,b):
  myPen.penup()
  for x in range(-200,201):
    y = a * x + b
    myPen.goto(x,y)
    myPen.pendown()
  
  myPen.penup()
  myPen.goto(-180,180)
  
  equation = ""
  if a==0:
    equation = " y = " + str(b)
  else:
    if b>0:
      equation = " y = " + str(a) + "x + " + str(b) 
    elif b<0:
      equation = " y = " + str(a) + "x " + str(b) 
    else:
      equation = " y = " + str(a)

  myPen.write(equation, None, None, "12pt bold")


myPen.color("white")
drawAxis()
myPen.color("#FF59F7")
drawLine(1.5,-40)

screen.tracer(0)
SyntaxError: multiple statements found while compiling a single statement
>>> from turtle import Turtle, Screen

WIDTH, HEIGHT = 20, 15  # coordinate system size

def plotter(turtle, x_range):
    turtle.penup()

    for x in x_range:
        y = x / 2 + 3
        ivy.goto(x, y)
        turtle.pendown()

def axis(turtle, distance, tick):
    position = turtle.position()
    turtle.pendown()

    for _ in range(0, distance // 2, tick):
        turtle.forward(tick)
        turtle.dot()

    turtle.setposition(position)

    for _ in range(0, distance // 2, tick):
        turtle.backward(tick)
        turtle.dot()

screen = Screen()
screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH//2, HEIGHT/2)

ivy = Turtle(visible=False)
ivy.speed('fastest')
ivy.penup()
axis(ivy, WIDTH, 1)

ivy.penup()
ivy.home()
ivy.setheading(90)
axis(ivy, HEIGHT, 1)

plotter(ivy, range(-WIDTH//2, WIDTH//2))

screen.exitonclick()
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> import turtle
>>> import turtle as t
>>> import math
>>> t. penup()
>>> t. goto(-200,0)
>>> t. pendown()
>>> t. goto(200,0)
>>> t. penup()
>>> t. goto(0,-200)
>>> t. pendown()
>>> t. goto(0,200)
>>> t. penup()
>>> for x in range(-200,201)
SyntaxError: invalid syntax
>>> for x in range(-200,201):
	y = -2x*x
	
SyntaxError: invalid syntax
>>> for x in range(-200,201):
	y = -2x
	
SyntaxError: invalid syntax
>>> for x in range(-200,201):
	y = -2x**
	
SyntaxError: invalid syntax
>>> for x in range(-200,201):
	y = x**2
	t. goto(x,y)
	t. pendown()

	
t.penup()
t.goto(180,200)

