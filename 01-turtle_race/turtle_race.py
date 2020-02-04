from turtle import Turtle
from random import randint

daddy = Turtle()
daddy.color('blue')
daddy.shape('turtle')
daddy.penup()
daddy.goto(-160, 100)
daddy.pendown()

mummy = Turtle()
mummy.color('red')
mummy.shape('turtle')
mummy.penup()
mummy.goto(-160, 70)
mummy.pendown()

big_sis = Turtle()
big_sis.color('green')
big_sis.shape('turtle')
big_sis.penup()
big_sis.goto(-160, 40)
big_sis.pendown()

lil_sis = Turtle()
lil_sis.color('yellow')
lil_sis.shape('turtle')
lil_sis.penup()
lil_sis.goto(-160, 10)
lil_sis.pendown()

for movement in range(100):
    daddy.forward(randint(1,5))
    mummy.forward(randint(1,5))
    big_sis.forward(randint(1,5))
    lil_sis.forward(randint(1,5))

print("Daddy: " + str(daddy.xcor()))
print("Mummy: " + str(mummy.xcor()))
print("Big Sis: " + str(big_sis.xcor()))
print("Lil Sis: " + str(lil_sis.xcor()))

input("Press Enter to close")
