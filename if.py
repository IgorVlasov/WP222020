x = int( input() )

if 5 < x < 10:
  print(1)
elif x == 0:
  print("ввели ноль")
elif x % 2 == 0:
  print("ввели четное число")  

else:
  print(0)