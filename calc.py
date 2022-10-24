def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mult(a,b):
  return a*b

def div(a,b):
  if b == 0:
     print('Division Error!')
     return
  return a/b

def addM(arr):
  sum = 0
  for i in arr:
    if !isnumeric(i):
      print('what the fuk is wron with u!')
      return
    sum = sum + i
  return sum

def subM(arr):
  result = 0
  for i in arr:
    if !isnumeric(i):
      print('what the fuk is wron with u!')
      return
    result = result - i
  return result

def multM(arr):
  product = 1
  for i in arr:
    if !isnumeric(i):
      print('what the fuk is wron with u!')
      return
    product = product * i
  return product

def divM(arr):
  result = arr[0]
  if arr[0] == 0
    return 0
  for i in range(1,len(arr)):
    if !isnumeric(arr[i]):
      print('what the fuk is wron with u!')
      return
    if arr[i] == 0:
      print('Division Error!')
    result = result / arr[i]
  return result
  
  
  
  
    
