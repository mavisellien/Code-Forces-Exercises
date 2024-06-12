if __name__ == "__main__":
    num = int(input())
    for i in range(num):
      words = input()
      A, B = words.split()
      A = list(A)
      B = list(B)
      a = A[0]
      b = B[0]
      A[0] = b
      B[0] = a
      str1 = ""
      str2 = ""
 
    
      for ele in A:
        str1 += ele
        
      for ele in B:
        str2 += ele

      print(str1,str2)

