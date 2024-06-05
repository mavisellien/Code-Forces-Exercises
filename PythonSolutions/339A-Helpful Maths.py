if __name__ == "__main__":
    num = input().split("+")
    num.sort()
    s = ''
    for i in range(len(num)-1):
        num[i] = num[i] + "+"
        s += num[i]
    print(s+num[-1])
