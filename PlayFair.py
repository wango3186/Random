key = list(input())
alpha = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

temp = []
for index,i in enumerate(key):
  
  if i == 'j':
    i = 'i'
  if i in temp:
    continue
  else:
    temp.append(i)
  if i in alpha:
    alpha.remove(i)

crypt = iter(temp + alpha)
for i in range(5):
  print("{} {} {} {} {}".format(next(crypt),next(crypt),next(crypt),next(crypt),next(crypt)))