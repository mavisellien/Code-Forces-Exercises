if __name__ == "__main__":
    num = input()
    L, B = (int(x) for x in num.split())
    
    i = 0
    
    while L <= B:
        L = L*3
        B = B*2
        i += 1
    
    print(i)
