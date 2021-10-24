def reverse_simple(str):
  return str[::-1]

def reverse(str):
  revarr = []
  for i in range(len(str),0,-1):
    revarr.append(str[i-1])  
  return "".join(revarr)

print(reverse("bushra"))