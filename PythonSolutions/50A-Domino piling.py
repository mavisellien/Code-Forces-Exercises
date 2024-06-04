import math
if __name__ == "__main__":
    num = input()
    M, N = (int(x) for x in num.split())
    print(math.floor((M*N)/2))
