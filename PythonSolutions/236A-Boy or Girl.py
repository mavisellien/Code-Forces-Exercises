if __name__ == "__main__":
    word = input()
    lst = []
    num = []
    count = 0
    for i in word:
        lst.append(i)
    for _ in lst:
        if _ not in num:
            count += 1
            num.append(_)
    if count%2:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
