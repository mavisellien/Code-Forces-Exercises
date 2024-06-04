if __name__ == "__main__":
    num = int(input())
    lst = []
    for i in range(num):
        names = input()
        if names not in lst:
            lst.append(names)
            print("OK")
        elif names in lst:
            print(names + str(lst.count(names)))
            lst.append(names)
