HELP = """
help - список команд
add - добавить событие
showall - показать все события
remove - удалить событие
exit - закрыть программу
"""
exit = False
userUnswer = 0

todo = {}
print("Введите команду")
print("Для вывода списка команд введите help")

while exit == False:
  userUnswere = input()

  if userUnswere == "exit":
    exit = True
    continue
  elif userUnswere == "add":
    print("Событие добавлено")
  elif userUnswere == "rewove":
    print("Событие удалено")
  elif userUnswere == "showall":
    print("События добавлены")
  elif userUnswere == "help":
    print(HELP)
  else:
    print("Ты чё ввёл гений???")