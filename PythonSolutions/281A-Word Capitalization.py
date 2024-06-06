if __name__ == "__main__":
    word = input()
 
    s = ""
    lst = []
    for i in word:
        lst.append(i)
    lst[0] = lst[0].capitalize()
    for _ in lst:
        s += str(_)
    print(s)
