if __name__ == "__main__":
    num = input()
    n, k = (int(x) for x in num.split())
    
    
    X = 0
        
    scores = input().split()
    
    for score in scores:
        
        if int(score) > 0:
            
            if int(score) >= int(scores[k-1]):
                X += 1
            elif int(score) < int(scores[k-1]):
                X = X
        
        else:
            X = X
    
    print(X)
        
