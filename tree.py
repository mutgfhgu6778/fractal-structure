import turtle
def draw_tree(size):
    if size >= 20:
        turtle.forward(size) # 1
        # 画右边树
        turtle.right(20)
        draw_tree(size - 40) # 2
        # 画左边树
        turtle.left(40)
        draw_tree(size - 40)
        # 后退
        turtle.right(20)
        turtle.backward(size)
turtle.left(90)
draw_tree(80)
turtle.done()