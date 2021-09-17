
lst = ['for', 'science', 'a', 'computer', 'this', 'is', 'class']

arr = [64, 4, 97, 22, 38, 62, 55]

n = len(lst)

for i in range(n):


 for j in range(0, n - i - 1):
  temp = len(lst[j])
  temp2 = len(lst[j+1])
  print(temp)
  print(temp2)
  print(lst)

  if temp > temp2:
     lst[j], lst[j+1] = lst[j+1], lst[j]




print(lst)


