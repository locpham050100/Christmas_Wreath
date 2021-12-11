import turtle
from turtle import *

speed(0)
bgcolor("black")

# vòng hoa
pensize(2)
penup()
goto(0, -100)
pendown()

for i in range(13):
    for colours in ["forestgreen", "darkgreen", "limegreen"]:
        color(colours)
        circle(150)
        left(10)
        forward(20)

# nơ ruy băng
penup()
goto(-95, 110)
pendown()
color("darkred", "red")
begin_fill()
forward(200)
right(120)
forward(100)
right(120)
forward(200)
left(120)
forward(100)
end_fill()

# vòng tròn trong ruy băng
penup()
goto(-40, 160)
pendown()
begin_fill()
circle(30)
end_fill()

# dãy băng bên trái
penup()
goto(-25, 132)
pendown()
begin_fill()
right(20)
forward(130)
left(80)
forward(60)
left(118)
forward(150)
end_fill()

# dãy băng bên phải
begin_fill()
right(92)
forward(5)
right(80)
forward(150)
left(110)
forward(60)
left(89)
forward(139)
end_fill()

# trang trí màu vàng 1
penup()
goto(-150, 20)
pendown()
color("gold", "yellow")
begin_fill()
circle(10)
end_fill()

# trang trí màu vàng 2
penup()
goto(140, -50)
pendown()
begin_fill()
circle(10)
end_fill()

# trang trí màu vàng 3
penup()
goto(-30, -130)
pendown()
begin_fill()
circle(10)
end_fill()

# trang trí màu vàng 4
penup()
goto(120, 110)
pendown()
begin_fill()
circle(10)
end_fill()

# trang trí màu đỏ 1
penup()
goto(140, 40)
pendown()
color("darkred", "red")
begin_fill()
circle(10)
end_fill()

# trang trí màu đỏ 2
penup()
goto(-120, -80)
pendown()
begin_fill()
circle(10)
end_fill()

# trang trí màu đỏ 3
penup()
goto(60, -120)
pendown()
begin_fill()
circle(10)
end_fill()

# trang trí màu đỏ 4
penup()
goto(-135, 110)
pendown()
begin_fill()
circle(10)
end_fill()

# lời chúc
penup()
goto(-170, 250)
pendown()
color("white")
write("MERRY CHRISTMAS", font=("Arial", 25, "bold"))
penup()
goto(-215, -250)
pendown()
write("AND A HAPPY NEW YEAR", font=("Arial", 25, "bold"))
hideturtle()

turtle.mainloop()