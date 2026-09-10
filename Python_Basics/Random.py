import random

a=int(random.random()*10+1)
print(a)

b=random.randint(1,5)
print(b)

start=1
stop=10
step=2
c=random.randrange(start, stop, step)
print(c)

d=random.seed(10)
print(d)