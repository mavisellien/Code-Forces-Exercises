if __name__ == "__main__":
    line1 = input()
    line1 = line1.lower()
    #line1 = sorted(line1)
    
    line2 = input()
    line2 = line2.lower()
    #line2 = sorted(line2)
    
    if line1 > line2:
        print("1")
    elif line2 > line1:
        print("-1")
    else:
        print("0")
