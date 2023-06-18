import random
from hw_module import chess_random as chs2
# from hw_module import chess_q as chs
if __name__ == "__main__":

    n = 8
    # print(chs.queen(*([int(i) for i in input().split()] for i in range(n))))
    chs2.func_random(x=[int(i+1) for i in range(n)], y=random.sample(range(1, n+1), n), try_count=4)
