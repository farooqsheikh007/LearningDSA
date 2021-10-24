arr1=[1,3,7,9]
arr2=[4,5,8]
def merge_sorted(arr1,arr2):
  arr = arr1+arr2
  arr.sort()
  return arr
print(merge_sorted(arr1,arr2))

