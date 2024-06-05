if __name__ == "__main__":
    matrix = []
    
    for i in range(5):
        num = input().split()
        matrix.append(num)
    
    for a in range(5):
        for b in range(5):
            if matrix[a][b] == "1":
                print(abs(2-a) + abs(2-b))
