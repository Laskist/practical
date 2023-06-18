# from practical_task_1.task_6.hw_module import chess_random as chs2
import random
from hw_module import chess_random as chs2
from hw_module import task_6_2 as chs
if __name__ == "__main__":

    n = 8
    print(chs.queen(*([int(i) for i in input().split()] for i in range(n))))
    # chs2.func_random(x=[int(i+1) for i in range(n)], y=random.sample(range(1, 9), 8), try_count=4)
