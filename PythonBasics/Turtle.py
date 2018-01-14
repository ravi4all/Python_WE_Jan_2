Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Pen()
<turtle.Turtle object at 0x0000025CA4A18F60>
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> turtle.forward(200)
>>> turtle.left(90)
>>> a = "Hello"
>>> print(a)
Hello
>>> print(a)
Hello
>>> turtle.reset()
>>> for i in range(5):
	turtle.forward(200)
	turtle.left(90)

	
>>> turtle.reset()
>>> turtle = turtle.Pen()
>>> for i in range(30):
	turtle.forward(5*i)
	turtle.left(45)

	
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(5*i)
	turtle.left(45)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    turtle.circle(5*i)
  File "C:\Python36\lib\turtle.py", line 1991, in circle
    self._go(l)
  File "C:\Python36\lib\turtle.py", line 1605, in _go
    self._goto(ende)
  File "C:\Python36\lib\turtle.py", line 3179, in _goto
    self._update()
  File "C:\Python36\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> turtle.reset()
>>> for i in range(30):
	turtle.circle(5*i)
	print("Radius is",5*i)
	turtle.left(45)

	
Radius is 0
Radius is 5
Radius is 10
Radius is 15
Radius is 20
Radius is 25
Radius is 30
Radius is 35
Radius is 40
Radius is 45
Radius is 50
Radius is 55
Radius is 60
Radius is 65
Radius is 70
Radius is 75
Radius is 80
Radius is 85
Radius is 90
Radius is 95
Radius is 100
Radius is 105
Radius is 110
Radius is 115
Radius is 120
Radius is 125
Radius is 130
Radius is 135
Radius is 140
Radius is 145
>>> turtle.reset()
>>> turtle.speed(0)
>>> for i in range(30):
	turtle.circle(5*i)
	print("Radius is",5*i)
	turtle.left(45)

	
Radius is 0
Radius is 5
Radius is 10
Radius is 15
Radius is 20
Radius is 25
Radius is 30
Radius is 35
Radius is 40
Radius is 45
Radius is 50
Radius is 55
Radius is 60
Radius is 65
Radius is 70
Radius is 75
Radius is 80
Radius is 85
Radius is 90
Radius is 95
Radius is 100
Radius is 105
Radius is 110
Radius is 115
Radius is 120
Radius is 125
Radius is 130
Radius is 135
Radius is 140
Radius is 145
>>> 
