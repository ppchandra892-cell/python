import random
from random import choice
head=0
tail=0
for i in range(100):
    flip=random.choice(['heads','tails'])
    if flip=="heads":
        head=head+1
    else:
        tail=tail+1
print("no.of heads:",head)
print("no. OF tails:",tail)