while True:
  try:
    a = int(input("Введите значение a: "))
    a = int(a)
  except ValueError:
    print("Произошла ошибка, введено не целое число")
  try:
    b = int(input("Введите значение b: "))
    b = int(b)
  except ValueError:
    print("Произошла ошибка, введено не целое число")
  if a == int(a) and b == int(b):
    break
z = 2 * b
y = 2 * a
vfir = a ** z
vsec = b ** y
print(vfir - vsec)