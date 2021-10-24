large = ['nemo'] * 10000
import time
def findNemo(arr):
  tzero = time.time()
  for i in arr:
    if i == 'nemo':
      print("Found Nemo!")
  tone = time.time()
  print(tone-tzero)

findNemo(large)