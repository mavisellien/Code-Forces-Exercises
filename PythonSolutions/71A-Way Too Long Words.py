if __name__ == "__main__":
    num = int(input())
    for i in range(num):
        words = input()
        if len(words) <= 10:
            print(words)
        elif len(words) > 10:
            print(words[0]+str(len(words) - 2)+words[-1])
