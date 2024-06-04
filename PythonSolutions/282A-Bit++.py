if __name__ == "__main__":
    num = int(input())
    X = 0
    for i in range(num):
        operations = input()
        if "++" in operations:
            X += 1
        elif "--" in operations:
            X -= 1
    print(X)
