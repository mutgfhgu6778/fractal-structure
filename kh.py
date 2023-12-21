#科赫雪花
import turtle

def koch(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        koch(t, length/3, depth-1)
        t.left(60)
        koch(t, length/3, depth-1)
        t.right(120)
        koch(t, length/3, depth-1)
        t.left(60)
        koch(t, length/3, depth-1)

def draw_koch_snowflake(t, length, depth):
    for _ in range(3):
        koch(t, length, depth)
        t.right(120)

# 创建一个画布和画笔
window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.color("blue")
pen.speed(0)

# 绘制科赫雪花
draw_koch_snowflake(pen, 300, 4)

# 关闭画布
window.exitonclick()