arr = [1,2,3,4,5,6,7]
x= 0
length = len(arr) - 1
print(len(arr))

while x < len(arr)/2:
    temp1 = arr[length - x]
    temp2 = arr[x]
    arr[x] = temp1
    arr[length - x] = temp2
    x += 1

print (arr)

success = 2
