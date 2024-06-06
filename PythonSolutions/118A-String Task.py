if __name__ == "__main__":
    word = input().lower()

    lst1 = []
    s = ""
    lst2 = []
    
    for i in word:
        lst1.append(i)
  
    
    for char in lst1:
        if char == "a" or char == "o" or char == "i" or \
        char == "u" or char == "e" or char == "y":
            continue
        else:
            char = "." + char
            lst2.append(char)
    
            
    for _ in lst2:
        s += _
    print(s) 
