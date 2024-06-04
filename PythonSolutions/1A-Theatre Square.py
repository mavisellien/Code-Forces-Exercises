import math
if __name__ == "__main__":
    num = input()
    n, m, a = (int(x) for x in num.split())
    print(math.ceil(n/a)*math.ceil(m/a))
