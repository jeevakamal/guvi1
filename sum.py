a=abs(int(input()))
suma = 0
while a>0:
  digit=a%10
  suma +=digit
  a=a//10
print("sum:",suma)
