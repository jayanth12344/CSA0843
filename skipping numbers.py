M = int(input("starting number of range: "))
N = int(input("ending number of range: "))
K = int(input("numbers to be skipped in range: "))
for i in range(M, N + 1, K):
   print(i)
