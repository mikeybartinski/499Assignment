arr = [64, 4, 97, 22, 38, 62, 55]

n = len(arr)

for i in range(n):


 for j in range(0, n - i - 1):


  if arr[j] > arr[j + 1]:
     arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)





print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),

