#皮亚诺曲线
import turtle

def peano_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        peano_curve(t, order-1, size/3)
        t.left(90)
        peano_curve(t, order-1, size/3)
        t.right(90)
        peano_curve(t, order-1, size/3)
        t.right(90)
        peano_curve(t, order-1, size/3)
        peano_curve(t, order-1, size/3)
        t.left(90)
        peano_curve(t, order-1, size/3)
        t.left(90)
        peano_curve(t, order-1, size/3)
        t.right(90)
        peano_curve(t, order-1, size/3)

# 创建一个画布和画笔
window = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔的初始位置和角度
pen.penup()
pen.goto(-200, -200)
pen.pendown()
pen.speed(0)

# 调用函数绘制皮亚诺曲线
peano_curve(pen, 4, 400)

# 关闭画布
window.exitonclick()
