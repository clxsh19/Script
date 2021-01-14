import turtle, random

def branch(branchlen,t):
    if branchlen > 5:   
        t.width(branchlen//5)    
        angle = random.randint(-30,30)
        diff = random.randint(5,15)

        t.forward(branchlen)
        t.right(angle)
        branch(branchlen-diff,t)
        t.left(angle + angle)
        branch(branchlen-diff,t)
        t.right(angle)

        if branchlen <= diff+10:
            t.color("green4")
        t.backward(branchlen)
        t.color("chocolate4")

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("chocolate4")
    branch(75,t)
    win.exitonclick()

main()