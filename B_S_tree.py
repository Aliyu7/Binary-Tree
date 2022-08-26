def binarySearch(array,x,low,high):
    if high >= low:
        mid = low + (high-low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array,x,low,mid-1)
        else:
            return binarySearch(array,x,mid+1,high)
    else:
        return -1
array = []
i = 1
while i < 20:
    array.append(i)
    i=i+1
x = int(input("Enter number between 1 and 20: "))
result = binarySearch(array,x,0,len(array)-1)
if result != -1:
    print("Element found at position "+str(result))
else:
    print("Element not found!")
