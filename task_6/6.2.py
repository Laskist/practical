import task_6_2 as chs

if __name__ == "__main__":

    n = 8
    print(chs.queen(*([int(i) for i in input().split()] for i in range(n))))

