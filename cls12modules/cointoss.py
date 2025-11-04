from random import choice
coin=["Head","Tail"]

head_count=0
for i in range(100):
    result=choice(coin)
    if result == "Head":
        head_count=head_count+1

print("No of Head Coin Flips:", head_count)
print("No of Tail Coin Flips:", 100-head_count)