if __name__ == "__main__":
    num = int(input())
    num_q = 0
    for i in range(num):
        views = input()
        if int(views[0])+int(views[2])+int(views[4]) >= 2:
            num_q += 1
        elif int(views[0])+int(views[2])+int(views[4]) < 2:
            num_q = num_q
    print(num_q)
