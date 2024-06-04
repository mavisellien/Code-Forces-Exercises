if __name__ == "__main__":
    num = int(input(""))
    lst_even = []
    lst_odd = []
    
    numbers = input().split()

    for number in numbers:
        if int(number)%2==0:
            lst_even.append(number)
        else:
            lst_odd.append(number)
    if len(lst_even) > len(lst_odd):
        for number in numbers:
            if int(number)%2:
                print(numbers.index(number)+1)
                
    elif len(lst_odd) > len(lst_even):
        for number in numbers:
            if int(number)%2 == 0:
                print(numbers.index(number)+1)
