while True:
  try:
    n = int(input())
  except:
    break

  num = 0
  i = 1
  while True:
    num = (1-10**i)//(1-10)
    if num % n == 0:
      print(i)
      break
    i+=1