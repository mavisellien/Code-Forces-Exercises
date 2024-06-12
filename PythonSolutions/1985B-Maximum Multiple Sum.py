if __name__ == "__main__":
  num = int(input())
  
  lst2 = []
  for i in range(num):
    lst = []
    n = int(input())
    lst2 = list(range(2, n+1))
    for x in range(2,n+1):
      k = 0
      x_sum = 0
      x_new = 0
      while x_new <= n:
        x_sum += k*x
        x_new += x
        k += 1
      lst.append(x_sum)

    index = lst.index(max(lst))
    print(lst2[index])
